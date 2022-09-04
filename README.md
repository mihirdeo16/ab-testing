# A/B-testing

![ab-testing-logo](https://raw.githubusercontent.com/mihir-workspace/ab-testing/main/assets/logo.png)

[![Pypi](https://img.shields.io/pypi/v/ab-testing-analysis?color=blue&logo=PyPI)](https://pypi.org/project/ab-testing-analysis/)
[![Read the Docs](https://img.shields.io/readthedocs/ab-testing-analysis?logo=Read%20the%20Docs&logoColor=blue)](https://ab-testing-analysis.readthedocs.io/en/latest/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ab-testing-analysis?color=orange)](https://pypi.org/project/ab-testing-analysis/)
[![release date](https://img.shields.io/github/release-date/mihirdeo16/ab-testing?color=blueviolet&logo=GitHub)](https://github.com/mihirdeo16/ab-testing/releases)
[![last commit](https://img.shields.io/github/last-commit/mihirdeo16/ab-testing?logo=git)](https://github.com/mihirdeo16/ab-testing/commits/main)

[![CICD](https://img.shields.io/github/workflow/status/mihirdeo16/ab-testing/Upload%20Python%20Package?color=%232088FF&label=CICD&logo=GitHub%20Actions)](https://github.com/mihirdeo16/ab-testing/actions/workflows/python-publish.yml)
[![Format](https://img.shields.io/pypi/format/ab-testing-analysis)](https://github.com/mihirdeo16/ab-testing)
[![License](https://img.shields.io/pypi/l/ab-testing-analysis)](https://github.com/mihirdeo16/ab-testing/blob/main/LICENSE)
[![size of files](https://img.shields.io/github/repo-size/mihirdeo16/ab-testing)](https://github.com/mihirdeo16/ab-testing)
---

A/B testing is process which allows developer/data scientist to analyze and evaluate, the performance of products in an experiment. In this process two or more versions of a variable (web page, page element, products etc.) are shown to different segments of website visitors at the same time to determine which version leaves the maximum impact and drives business metrics.

In A/B testing, **A** refers to the original testing variable. Whereas **B** refers to a new version of the original testing variable. Impact of the results can be evaluated based on,
+ Conversion Rate
+ Significance test

----
#### Documentation can be found on- [ab-testing-analysis.readthedocs.io](https://ab-testing-analysis.readthedocs.io/en/latest/)
----

## Installation & Usage

+ Installing the library from [pypi](https://pypi.org/project/ab-testing-analysis/) - It has only dependency on *pandas & numpy*
```shell
pip install ab-testing-analysis
```
+ Usages & working sample - [Tutorial](https://colab.research.google.com/github/mihirdeo16/ab-testing/blob/main/docs/Tutorial.ipynb)

+ Example code, 

```python
from ab_testing import ABTest
from ab_testing.data import Dataset

df = Dataset().data()

ab_obj = ABTest(df,response_column='Response',group_column='Group')

print(ab_obj.conversion_rate(),'\n','-'*10)
print(ab_obj.significance_test(),'\n','-'*10)
print(df.head())
```
Output:
```shell
  Conversion Rate Standard Deviation Standard Error
A          20.20%              0.401          0.018
B          22.20%              0.416         0.0186 
 ----------
z statistic: -0.77      p-value: 0.439
Confidence Interval 95% for A group: 16.68% to 23.72%
Confidence Interval 95% for B group: 18.56% to 25.84%

The Group A fail to perform significantly different than group B.
The P-Value of the test is 0.439 which is above 0.05, hence Null hypothesis Hₒ cannot be rejected. 
 ----------
        Users  Response Group
0  IS36FC7AQJ         0     A
1  LZW2YNYHZG         1     A
2  9588IGN0RN         1     A
3  HSAH1TYQFF         1     A
4  5D9G147941         0     A

```
## Contribution
All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

A detailed overview on how to contribute can be found in the [contributing guide](https://ab-testing-analysis.readthedocs.io/en/latest/Contribution.html).

## Code of Conduct
As contributors and maintainers to this project, you are expected to abide by code of conduct. More information can be found at [Code of conduct](https://ab-testing-analysis.readthedocs.io/en/latest/Code_of_conduct.html)

## License
[MIT ](https://ab-testing-analysis.readthedocs.io/en/latest/Licence.html)




