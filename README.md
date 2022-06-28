# A/B-testing

![ab-testing-logo](assets/logo.png)

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
A          20.60%              0.404        0.0181
B          19.00%              0.392        0.0176 
 ----------
z statistic: 0.63	p-value: 0.526
Confidentce Interval 95% for A group: 17.06% to 24.14%
Confidentce Interval 95% for B group: 15.56% to 22.44%

The Group A fail to performe significantly different than group B.
The P-Value of our test is 0.526 which is above 0.05, hence Null hypothesis Hₒ cannot be rejected. 
 ----------
        Users  Response Group
0  ZVFCUQFMK5         0     A
1  Y52C42LLKG         1     A
2  NCC1CC173U         0     A
3  4TR4XAT6Q7         0     A
4  XCJTBHI70P         0     A

```

## License
[MIT ](LICENSE)




