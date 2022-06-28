# A/B-testing

![ab-testing-logo](https://raw.githubusercontent.com/mihir-workspace/ab-testing/main/assets/logo.png)

[![Pypi](https://img.shields.io/pypi/v/ab-testing-analysis?color=blue)](https://pypi.org/project/ab-testing-analysis/)
[![Format](https://img.shields.io/pypi/format/ab-testing-analysis)](https://github.com/mihir-workspace/ab-testing)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ab-testing-analysis)](https://pypi.org/project/ab-testing-analysis/)
[![License](https://img.shields.io/pypi/l/ab-testing-analysis)](https://github.com/mihir-workspace/ab-testing/blob/main/LICENSE)
[![SocialMedia](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FDeoMihir_7)](https://twitter.com/DeoMihir_7)

---

A/B testing is process which allows developer/data scientist to analyze and evaluate, the performance of products in an experiment. In this process two or more versions of a variable (web page, page element, products etc.) are shown to different segments of website visitors at the same time to determine which version leaves the maximum impact and drives business metrics.

In A/B testing, **A** refers to the original testing variable. Whereas **B** refers to a new version of the original testing variable. Impact of the results can be evaluated based on,
+ Conversion Rate
+ Significance test
----

## Installation & Usage
+ Installing the library from [pypi](https://pypi.org/project/ab-testing-analysis/) - It has only dependency on *pandas & numpy*
```shell
pip install ab-testing-analysis
```
+ Usages & working sample - [Tutorial](https://github.com/mihir-workspace/ab-testing/blob/main/Docs/Tutorial.ipynb)
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
  Conversion Rate Standard Deviation Standar Error
A          19.80%              0.398        0.0178
B          18.80%              0.391        0.0175 
 ----------
z statistic: 0.40	p-value: 0.689
Confidence Interval 95% for A group: 16.31% to 23.29%
Confidence Interval 95% for B group: 15.38% to 22.22%

The Group A fail to perform significantly different than group B.
The P-Value of the test is 0.689 which is above 0.05, hence Null hypothesis Hₒ cannot be rejected. 
 ----------
        Users  Response Group
0  7PI90FXM9P         0     A
1  24WYZXYSO2         0     A
2  A2APLMELIB         0     A
3  XMU2COFEWQ         0     A
4  B9L2IKKMBD         0     A

```

## License
[MIT ](LICENSE)




