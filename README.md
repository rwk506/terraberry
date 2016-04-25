![terraberry](https://github.com/rwk506/terraberry/blob/master/images/logo.png)

<h3>Defending the health of the Earth one conscientious choice at a time.</h3>

Human-powered destruction of the Earth will continue to ravage our planet -- unless we take more steps to stop it. terraberry enables people to make better choices conveniently and conscienciously in their daily lives to defend and promote a healthier Earth - EVERY purchase, EVERY day.

The code presented here is the python backend of the terraberry application, which facilitates sustainable and habitual lifestyle choices to improve the health of the Earth. terraberry allows users to scan the barcode of an item in store, determine if ingredients are harmful to the environment, and provides consumers with the ability to make choices to reduce the detrimental impact on the Earth through their everyday purchases.

This development is brought to you by the first place finish terraberry team via the [Space Apps Orlando](https://2016.spaceappschallenge.org/challenges/tech/bring-your-own-solution/projects/terraberry-defend-the-earth) as part of the [Bring Your Own Solution Challenge](https://2016.spaceappschallenge.org/challenges/tech/bring-your-own-solution/).

<br />

<h4>Table of Contents</h4>
[Summary](#Summary)<br />
[Example](#Example)<br />
[Environmental Impact](#Impact)<br />
[Documentation](#Docs)<br />
[Resources](#Resources)<br />
[Dependencies](#Deps)<br />
[Other Information](#Other)<br />


<img src="https://github.com/rwk506/terraberry/blob/master/images/twitterlogo.png" alt="Twitter" width="50" height="50">
<img src="https://github.com/rwk506/terraberry/blob/master/images/FBlogo.png" alt="Facebook" width="50" height="50">
<img src="https://github.com/rwk506/terraberry/blob/master/images/inboxlogo.png" alt="Gmail" width="60" height="55">

<br /><br />



<a name="Summary"/>
<h4>Summary</h4>

Our project enables citizens to use their smartphones when making a purchase to determine whether harmful materials are present in a product. On a daily basis, users can conveniently make informed choices about the products they are buying, while educating themselves about the devastating effects of materials like palm oil, silicates, and triclosan on the well-being of the Earth.

The application will be able to read the barcode of an item, whether food or household. While in a store, a user can whip out their phone, scan an item they are interested in purchasing, and our app informs the user whether the harmful ingredients of palm oil, silicates, or triclosan are present in the item. We also incorporate an informative component to educate users on the world-wide effects of these damaging ingredients. Our product will foster awareness and grant consumers the opportunity to make a conscientious choice about how their purchases affect the environment.




<br /> <br /><br />

<a name="Example"/>
<h4>Example</h4>

Our android app will be available for download, and on startup will look like the middle image below. 

![terraberry Start Screen](https://github.com/rwk506/terraberry/blob/master/images/start_screen.png | width=100)

![Triclosan Home](https://github.com/rwk506/terraberry/blob/master/images/triclosan_home.png | width=100)

![Clorox terraberry Results](https://github.com/rwk506/terraberry/blob/master/images/results_clorox.png | width=100)








<br /> <br /><br />

<a name="Impact"/>
<h4>Environmental Impact</h4>

The collection of materials such as silicates and palm oil are damaging to ecological systems, affecting habitats of endangered species as well as contributing in the decline of air and water quality across the globe. 













<br /> <br /><br />

<a name="Docs"/>
<h4>Documentation</h4>

The source code and necessary data files may all be downloaded as a zip, forked, or cloned on a local machine from the [terraberry](https://github.com/rwk506/terraberry) repository.

The primary Python scripts included is **HackHTML.py**, where the primary function used to determine whether harmful ingredients are present is **lookup_barcode()**. The frontend android barcode reader will pass the barcode/UPC number to the python script, which will then determine whether silicates, palm oil, triclosan, or their derivatives are present in the scanned product. The results of this are passed back to the front-end of the application.

The files included are in this repository are:

- **HackHTML.py**: primary code that does searching and cross-correlation of databases/ingredients
- **HouseholdDB.txt**: list of IDs for household items in NIH/NLM library
- **oils.txt**: list of palm oil aliases and derivates
- **silicates.txt**: list of silicate aliases and derivates
- **triclosan.txt**: list of triclosan aliases and derivatives


If the user has Python and the necessary packages installed, no further installation should be required to run the code. If scripted, code may be run from outside Python with the command-line call 'python example.py' (where example is the name of the script). If inside Python, the functions lookup\_barcode() may be called following importing the necessary packages and:

    import HackHTML.py as HH  ### import python code
    HH.lookup_barcode()  ### function call







<br /> <br /><br />

<a name="Resources"/>
<h4>Resources</h4>
The following websites and databases were used in this project:
[Android Studio](http://developer.android.com/tools/studio/index.html)<br />
[Android Barcode Reader](https://github.com/zxing/zxing)<br />
[Environmental Working Group](http://www.ewg.org/)<br />
[US Department of Health and Human Services](https://householdproducts.nlm.nih.gov)<br />
[UPC Lookup Database](http://www.upcitemdb.com/)<br />
[NASA Worldview](https://worldview.earthdata.nasa.gov/)<br />
[World Wildlife Federation](http://www.worldwildlife.org/)<br />



<br /> <br /><br />

<a name="Deps"/>
<h4>Dependencies</h4>

This Python code was written using Python 2.7 and Numpy 1.10.4, but should be compatible with many other versions. The user may have to install the html, urllib2, re, or cookielib libraries.

Compatible with iPython Notebook (use %run [name]).




<br /> <br /><br />

<a name="Other"/>
<h4>Other Information</h4>

Contributors: RWK, TDM, KA, WM <br />
Contact: May be made through GitHub. <br />
<br />


