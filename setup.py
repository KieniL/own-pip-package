import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='helloworld_kienast',  

     version='0.1',

     scripts=['helloworld'] ,

     author="Lukas Kienast",

     author_email="lukaskienast0@gmail.com",

     description="A test package",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/Kreidl/own-pip-package",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )