import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    # Here is the module name.
    name="kaironviz",
 
    # version of the module
    version="0.0.2",
 
    # Name of Author
    author="Kairon Team, Nimblework",
 
    # your Email address
    author_email="spandan.mondal@nimblework.com",
 
    # #Small Description about module
    description="Data visualization for notebooks and html export",
 
    # long_description=long_description,
 
    # Specifying that we are using markdown file for description
    long_description=long_description,
    long_description_content_type="text/markdown",
 
    # Any link to reach this module, ***if*** you have any webpage or github profile
    # url="https://github.com/username/",
    packages=setuptools.find_packages(),
    include_package_data=True,
 
 
    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
 
 
 
    install_requires=[
        "pandas",
        "ipython",
        "jsmin",
    ],
 
 
    license="MIT",
 
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)