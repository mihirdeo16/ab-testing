========================
Usage & API reference
========================

Usage
-------

To use the different functionalities/modules of library, create a object of the class `ABTest` with passing 
class parameters,

+ :code:`df` = A dataframe which has Users, Response column and Group column
+ :code:`response_column` = A binary valued column's name which has 1 or 0 correspond for the users which being converted or not respectively.
+ :code:`group_column` = A binary valued column's name which will indicate the user belong to which group **A** or **B** group.
+ :code:`labels` = (Optional) An array with two string values which will label of the :code:`group_column`.

Example Code
`````````````
Below is example code snippet of the functionality and sample dataframe.

.. code:: python

   from ab_testing import ABTest
   from ab_testing.data import Dataset

   df = Dataset().data()

   abtest_obj = ABTest(df,response_column='Response',group_column='Group')

   print(abtest_obj.conversion_rate(),'\n','-'*10)
   print(abtest_obj.significance_test(),'\n','-'*10)
   print(df.head())

Output:

.. code:: shell

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


APIs/Functions
---------------

Conversion rate :code:`conversion_rate`
`````````````````````````````````````````
It provides the conversion rate along with standard deviation and standard error values for each group. 
It return the these values in table format in pandas dataframe type.

.. note::

   .. code:: python

      abtest_obj.conversion_rate()

   **Output:**  

   .. code:: shell

      Conversion Rate Standard Deviation Standard Error
      A          20.20%              0.401          0.018
      B          22.20%              0.416         0.0186 


Significance test :code:`significance_test`
`````````````````````````````````````````````
This provides the significance test report in along with conclusive statement. It provides following information,

+  Confidence Interval of 95% for each group.
+  P-Value for between group **A** and **B**.
+  Z-statistic for between group **A** and **B**.
  
:code:`significance_test` parameter,

+ :code:`threshold` = (Optional) To set the P-Value threshold for the significance test, a float value between 0 to 1.

.. note::

   .. code:: python

      abtest_obj.significance_test() 

   **Output:**

   .. code:: shell

         z statistic: -0.77      p-value: 0.439
         Confidence Interval 95% for A group: 16.68% to 23.72%
         Confidence Interval 95% for B group: 18.56% to 25.84%

         The Group A fail to perform significantly different than group B.
         The P-Value of the test is 0.439 which is above 0.05, hence Null hypothesis Hₒ 
         cannot be rejected.