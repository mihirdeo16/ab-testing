from setuptools import find_packages, setup 
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '1.2.7'
DESCRIPTION = "AB test analysis toolbox for analyzing and reporting the results of an ab test experiment. It provides the functions to analyze the ab test result of an experiment."

# Setting up
setup(
    name="ab_testing-analysis",
    version=VERSION,
    author="Mihir Deo",
    author_email="<mihirdeo16@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,

    project_urls={
    'Homepage' : 'https://ab-testing-analysis.readthedocs.io/en/latest/index.html',
    'Documentation': 'https://ab-testing-analysis.readthedocs.io/en/latest/Getting_Started.html',
    'Source': 'https://github.com/mihirdeo16/ab-testing',
    'Tracker': 'https://github.com/mihirdeo16/ab-testing/issues',
    },

    packages= find_packages(),
    install_requires=["pandas","statsmodels"],
    keywords=['python','ab test' ,'ab testing', 'ab testing analysis','abtesting analysis','abtesting', 
                'response analysis','conversion rate analysis','statistical test'],
    
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",

        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",

        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",


    ]
)
