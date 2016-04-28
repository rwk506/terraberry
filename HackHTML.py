
# coding: utf-8


###############################################################
######### Authored by: Team Hush Yuppies @ UF Astro   #########
###############################################################


import os
import html
import urllib2, cookielib
from urllib2 import Request
import re, string
import operator
import image
from IPython.display import Image, display



def compare_to_chemicals(ingd):

    oils = np.loadtxt('./oils.txt', np.dtype({'names':['names'], 'formats':['S99']}) , delimiter='\n')
    silicates = np.loadtxt('./silicates.txt', np.dtype({'names':['names'], 'formats':['S99']}) , delimiter='\n')
    triclosan = np.loadtxt('./triclosan.txt', np.dtype({'names':['names'], 'formats':['S99']}) , delimiter='\n')
    phals = np.loadtxt('./phthalates.txt', np.dtype({'names':['names'], 'formats':['S99']}) , delimiter='\n')
    formeld = np.loadtxt('./formaldehyde.txt', np.dtype({'names':['names'], 'formats':['S99']}) , delimiter='\n')
    
    YNlist = ['No', 'No', 'No', 'No', 'No']
    
    for f, aliaslist in enumerate([oils, silicates, triclosan, phals, formeld]):
        ##### set up each ingredient entry as a list of words
        for j,ingred in enumerate(ingd):
            ing = ingred.lstrip(' ').split(' ')
            #print ingred
            ##### set up each database check entry as a list of words
            for i,val in enumerate(aliaslist):
                val[0] = val[0].replace(',', '')
                full_list = val[0].split()
                #### check to see if all words are in list
                switches = [0]*len(ing)   ### create "on/off" switches to represent no(0) and yes(1) for each word in ingredient list
                for k, word in enumerate(full_list):
                    for m,sw in enumerate(ing):
                        ind_ingred = re.sub(r'[^\w]', '', ing[m])
                        if len(re.findall(str(ind_ingred),str(word), re.IGNORECASE))>0:
                            switches[m]=1  ## if ingredient word is a match, turn switch to yes
                            break
                if sum(switches)==len(switches):  ### if all words are present in an alias, then turn overall oil content to yes
                    YNlist[f] = 'Yes'
                  
    chem = [r"Palm Oil present:"+'\t', r"Silicates present:"+'\t', r"Triclosan present:"+'\t', r"Phthalates present:"+'\t', r"Formaldehyde present:"+'\t']
    for i,res in enumerate(YNlist):
        print chem[i],res
        
    return YNlist




def compare_to_ProductDB(ingd):

    #### load in DB file
    DBtbl = open("./HouseholdDB.txt", "rw+")
    file_content = DBtbl.readlines()
    DBtbl.close()
    
    for j,ingred in enumerate(ingd):
        ingred = ingred.lstrip(' ')
        regex = re.compile('[,-\."!?&\[\]\(\)\/(>)(<)]')
        ingred = regex.sub('', ingred)
        ing = string.split(ingred)
        listA = [s.lower() for s  in ing]
        
        correl=[]
        ##### set up each database check entry as a list of words
        for i,val in enumerate(file_content):#[0:600]):
            product = re.search(r'">(.*)</A>', val).group(1) 
            product = regex.sub('', product)
            full_list = product.split(' ')
            listB = [s.lower() for s in full_list]
            listB = listB
            
            ##### look at amount of intersection between database and ingredient list
            Intsect = list(set(listA) & set(listB))
            #print Intsect, float(len(Intsect))/float(len(listA))#, listA, listB
            correl.append(float(len(Intsect))/float(len(listA)))
            
        max_index, max_value = max(enumerate(correl), key=operator.itemgetter(1))
        IDnum = re.search(r'&id=.*"', file_content[max_index]).group(0)
        IDnum = IDnum.strip('"&id=')
        
    return IDnum




def lookup_barcode(barcode):
    site= 'http://www.ewg.org/foodscores/products?search='+str(barcode)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    req = urllib2.Request(site, headers=hdr)

    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    ### read in page
    content = page.read()
    ### find next page, where we will be able to grab html and get ingredients
    findstr = r'<a href="/foodscores/products/\d*'+str(barcode)+'\d*-\W*'
    result = re.findall(findstr, content)


    ########## If there is a matching result in the food database (len>0), move forward here
    if len(result)>0:        
        #### grab page, using previous result, to go to webpage with the ingredients 
        nextpage = 'http://www.ewg.org'+result[0][9:]
        req = urllib2.Request(nextpage, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        content = page.read()  ### read page
        findstr = r'From the Package</h2>\n<p>.*.</p>'  ### find string that has the ingredients
        result2 = re.findall(findstr, content)
        #### print name
        findstr = r"<title>EWG's Food Scores .*</title>"
        prod_name = re.findall(findstr, content)
        print prod_name[0][27:-8]


        #### break up the ingredients into a list
        ingredients = re.search(r'\<p>(.*)\.</p>', result2[0]).group(1)
        ingd = ingredients.split(',')

        ### will compare to oils, silicates, and triclosan respectively and give 'yes' or 'no' for presence of each
        YNlist = compare_to_chemicals(ingd)


    ########### If there is no match in the food database, we move forward with the household database
    if len(result)==0:
        household = 'http://www.upcitemdb.com/upc/'+str(barcode)
        req = urllib2.Request(household, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        content = page.read()
        findstr = r' associated with <b>.*</b>'#<b>.*</b>'
        result2 = re.findall(findstr, content)

        ### product name isolation
        product = re.search(r'\<b>(.*)</b>', result2[0]).group(1)
        print product
        
        ### go to a new page using database of product names, after matching
        webpage = 'https://householdproducts.nlm.nih.gov/cgi-bin/household/list?tbl=TblBrands&alpha='+product[0]
        req = urllib2.Request(webpage, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        content = page.read()            #### read in content
        
        #### find/extract ingredients
        IDnum = compare_to_ProductDB([product])#; print IDnum, product
        webpage2 = 'https://householdproducts.nlm.nih.gov/cgi-bin/household/brands?tbl=brands&id='+IDnum
        req = urllib2.Request(webpage2, headers=hdr)
        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()
        
        content = page.read()            #### read in content
        findstr = r'chem&id=.*</a>'
        result2 = re.findall(findstr, content, re.MULTILINE)
        ingredients=[]
        for i in np.arange(0,len(result2)):
            ingredients.append(result2[i][12:-4])
        print ingredients
        YNlist = compare_to_chemicals(ingredients)
        
    return content




#### Food Items - Examples

# Larabar Blueberry Muffin
content = lookup_barcode('2190850737')

# French Marin Delicate Petite Blue Cheese, Soft Ripened Cheese
content = lookup_barcode('074310201006')

# Sides Knorr Knorr, Pasta Sides, Fettuccini In A Delicate Butter Flavored Sauce, Butter Flavor
content = lookup_barcode('041000022494')

# Cheez It Cheese It Baked Snack Crackers, Mozzarella
content = lookup_barcode('024100789177')

# Nutella Hazelnut Spread With Cocoa
content = lookup_barcode('0980089525')

# Eden Eden, Organic Black Beans
content = lookup_barcode('024182002539')



#### Household - Examples


# Clorox Anywhere Hard Surface Spray
content = lookup_barcode('44600016832')

# Anywhere Sanitizing Spray, 22 oz. Trigger Spray Bottle
content = lookup_barcode('4460001683')

# Softsoap Hand Soap Lavender & Chamomile
content = lookup_barcode('074182292171')

# Ultra Antibacterial Hand Soap Dishwashing Liquid, Orange Scent, 30 Ounce
content = lookup_barcode('037000110880')

# Red Devil  0694 Panel and Foam Adhesive, 10.1-Ounce
content = lookup_barcode('075339013953')

# Sally Hansen 5 Minute French Manicure White Tip Pen-Fine Point, 0.16 Fluid Ounce
content = lookup_barcode('074170310009')


