import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="kaironviz",
 
    version="0.0.2",
 
    author="Kairon Team, Nimblework",
 
    author_email="spandan.mondal@nimblework.com",
 
    description="Data visualization for notebooks and html export",
 
    long_description=long_description,
    long_description_content_type="text/markdown",
 

    packages=setuptools.find_packages(),
    include_package_data=True,

 
    install_requires=[
        "pandas",
        "ipython",
        "jsmin",
    ],

 
    license="MIT",
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)