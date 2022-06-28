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

ab_obj = ABTest(df,response_column='converted',group_column='group')

print(ab_obj.conversion_rate())
```
Output:
```shell
  Conversion Rate Standard Deviation Standar Error
A          19.80%              0.398        0.0178
B          20.20%              0.401         0.018
```
**Significance Test**,
```python 
print(ab_obj.significance_test())
```
Output:
```
z statistic: -0.46	p-value: 0.644
Confidentce Interval 95% for A group: 17.24% to 24.36%
Confidentce Interval 95% for B group: 18.37% to 25.63%

The Group A fail to performe significantly different than group B.
The P-Value of our test is 0.644 which is above 0.05, hence Null hypothesis Hₒ cannot be rejected.

```

## License
[MIT ](LICENSE)




