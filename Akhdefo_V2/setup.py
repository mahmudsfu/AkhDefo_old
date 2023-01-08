from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='akhdefo_functions',
    version='2.1.01',    
    description='Land Deformation Monitoring Using Optical Satellite Imagery',
    url='https://github.com/mahmudsfu/AkhDefo',
    author='Mahmud Mustafa Muhammad',
    author_email='mahmud.muhamm1@gmail.com',
    license='Academic Free License (AFL)',
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["Akhdefo_Coreg", 'AkhDefo_Tools', 'AkhDefo_TS', 'Akhdefo_utils'
    , 'AkhdefoPlot','Filter_PreProc','Mosaic_Crop','OpticalFlow', 'Stacked_Velocity', 'Unzip_CopyFiles' ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Academic Free License (AFL)',  
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',  'Programming Language :: Python :: 3.6',  
        'Programming Language :: Python :: 3.7', "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

    ])


 