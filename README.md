# A/B-testing

![ab-testing-logo](https://raw.githubusercontent.com/mihir-workspace/ab-testing/main/assets/abtest_logo.png)

A/B testing is process which allows developer/data scientist to analyze and evaluate, the performance of products in an experiment. In this process two or more versions of a variable (web page, page element, products etc.) are shown to different segments of website visitors at the same time to determine which version leaves the maximum impact and drives business metrics.

In A/B testing, **A** refers to ‘control’ or the original testing variable. Whereas **B** refers to ‘treatment’ or a new version of the original testing variable. Impact of the results can be evaluated based on,
+ Conversion Rate
+ Significance test
----

#### Installation & Usage
+ Installing the library from [pypi](https://pypi.org/project/ab-testing-analysis/) - It has only dependency on *pandas & numpy*
```shell
pip install ab-testing-analysis
```
+ Usages & working sample - [Tutorial](https://github.com/mihir-workspace/ab-testing/blob/main/Docs/Tutorial-walkthrough.ipynb)
```python
from ab_testing import ABTest
ab_obj = ABTest(df,response_column='converted',group_column='group')

print(ab_obj.conversion_rate())
```
![Conversion-rate](https://raw.githubusercontent.com/mihir-workspace/ab-testing/main/assets/results-conversion-rate.png)






