# A/B-testing

![ab-testing-logo](https://raw.githubusercontent.com/mihir-workspace/ab-testing/main/assets/abtest_logo.png)

[![License](https://img.shields.io/pypi/v/ab-testing-analysis)](https://pypi.org/project/ab-testing-analysis/)
[![License](https://img.shields.io/pypi/l/ab-testing-analysis)](https://github.com/mihir-workspace/ab-testing/blob/main/LICENSE)
[![License](https://img.shields.io/pypi/format/ab-testing-analysis)](https://github.com/mihir-workspace/ab-testing/blob/main/LICENSE)
[![License](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FDeoMihir_7)](https://twitter.com/DeoMihir_7)

---

A/B testing is process which allows developer/data scientist to analyze and evaluate, the performance of products in an experiment. In this process two or more versions of a variable (web page, page element, products etc.) are shown to different segments of website visitors at the same time to determine which version leaves the maximum impact and drives business metrics.

In A/B testing, **A** refers to the original testing variable. Whereas **B** refers to a new version of the original testing variable. Impact of the results can be evaluated based on,
+ Conversion Rate
+ Significance test
----

### Installation & Usage
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

## License
[MIT ](LICENSE)




