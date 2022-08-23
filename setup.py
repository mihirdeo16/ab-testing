from setuptools import find_packages, setup 
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.2.6'
DESCRIPTION = "A/B testing analysis toolbox for monitoring and reporting experiment results"

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
    'Homepage' : 'https://github.com/mihir-workspace/ab-testing',
    'Documentation': 'https://github.com/mihir-workspace/ab-testing#readme',
    'Funding': 'https://donate.pypi.org',
    'Source': 'https://github.com/mihir-workspace/ab-testing',
    'Tracker': 'https://github.com/mihir-workspace/ab-testing/issues',
    },

    packages= find_packages(),
    install_requires=["pandas","statsmodels"],
    keywords=['python', 'a/b testing', 'abtest','abtesting', 'response analysis','conversion rate analysis','statistical test'],
    
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",

        "Development Status :: 5 - Production/Stable",

        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        

        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",


    ]
)
