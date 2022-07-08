from setuptools import find_packages, setup 
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.2.5'
DESCRIPTION = 'A python library dedicated for A/B testing analysis for experiment testing'

# Setting up
setup(
    name="ab_testing-analysis",
    version=VERSION,
    author="Mihir Deo",
    author_email="<mihirdeo16@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/mihir-workspace/ab-testing',
    packages= find_packages(),
    install_requires=["pandas==1.4.2","statsmodels==0.13.2"],
    keywords=['python', 'a/b testing', 'abtest','abtesting', 'response analysis','conversion rate analysis','statistical test'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)