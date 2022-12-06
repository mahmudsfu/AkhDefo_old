# AkhDefo
 Computer Vision for Slope Stability
 
 # Note: Version 2 of Akhdefo will be released soon. 
 **Main Changes:
 **-The new version mainly is built on GDAL and Rasterio Libraries.
 -Tkinter Simple GUI removed
 -Akhdefo now can run on cloud processing
 -Akhdefo now consist of 12 Modules that performs end to end  python-based GIS and Image Processing and Custumized Figure generation
 
 #Recommended Citation:
 
Muhammad M, Williams-Jones G, Stead D, Tortini R, Falorni G and Donati D (2022) Applications of ImageBased Computer Vision for Remote
Surveillance of Slope Instability.Front. Earth Sci. 10:909078. doi: 10.3389/feart.2022.909078

Background of Akh-Defo: AKh-Defo is combination of two different words 1) Akh in Kurdish language means land, earth or soil (origion of the word is from Kurdish badini dailect) 2) Defo is short of English word deformation.
 
#To setup the software environment and install the required python libraries follow the below steps:

####step1 Install Anaconda for Windows

https://www.anaconda.com/products/individual?modal=commercial

##step 2 Create new Anaconda environment called akhdefo using the below command. 
Please copy the akh-defo.txt and akhdeforequirements.txt files and paste them at C:\Users\your windows username folder  then run the following command

conda create --name akhdefo --file akh-defo.txt

###Step 3 Activate the newly created anaconda environment using the below command

conda activate akhdefo

##step 4 run the below command to install the remaining required python libraries.

pip install -r akhdeforequirements.txt

Congrats Now your python environment ready to run the Akh-Defo software

Optional Step: its highly recommned to install Visual studio code to run Akh-Defo software, Although you can run the software on any python IDE as long as you choose the akhdefo conda environment as python interpreter 

If you use jupyter notebook or JupyterLab make sure you have also installed ipython and ipkerenel 




