# Import the required lib
import pandas 
import numpy as np
from statsmodels.stats.proportion import proportions_ztest, proportion_confint


class ABTest:

    def __init__(self,df_A:pandas.DataFrame,response_column:str, df_B:pandas.DataFrame=None,
                            group_column:str=None,labels = ['A','B']) -> None:
        """
        The function takes in either one DataFrame or two dataframes, and a column name for the response
        variable. It then creates a new object with attributes for the two dataframes, the response
        variable, and the group labels
        
        :param df_A: The first dataframe
        :type df_A: pandas.DataFrame

        :param response_column: The column name of the response variable.
                                Value in the response column should be 0&1 to indicating the unsucessful and successful.
        :type response_column: str

        :param df_B: The second dataframe
        :type df_B: pandas.DataFrame

        :param group_column: The column name that indicates the group
        :type group_column: str

        :param labels: The labels for the two groups Optional
        """

        # Check the unique values in response column and raise error if not binary
        if df_A[response_column].nunique() !=2:
                raise ValueError('Response column should contain binary values')
        # Set the response column name 
        self.response_column = response_column

        # Check the group column is none or not it not means Single DF contain both A & B set
        if group_column !=None:
            # Set the group column
            self.group_column = group_column

            # Check the unique values in group_column and raise error if not binary
            if df_A[self.group_column].nunique() !=2:
                raise ValueError('Group column should contain two distinct values indicating A&B set')

            # Take group element values & Create two DF by slicing the Master DF
            self.groups_ele = list(df_A[self.group_column].unique())
            self.a_sample = df_A[df_A[self.group_column]==self.groups_ele[0]]
            self.b_sample  = df_A[df_A[self.group_column]==self.groups_ele[1]] 

            # Assigned the group element as Labels
            self.a_label = self.groups_ele[0]
            self.b_label = self.groups_ele[1]

        # Check if DF B is give or not
        elif df_B !=None:

            # Assigned the DF to right variables
            self.b_sample = df_B
            self.a_sample = df_A
            
            # Assigned the labels either default or given by the user.
            self.a_label = labels[0]
            self.b_label = labels[1]

        # Check either DF B is given or group_column else raise the error.
        elif df_B ==None and group_column==None:
            raise ValueError('Either provide the second dataframe(df_B) or give column name for group indication of A&B') 

    def conversion_rate(self) -> pandas.DataFrame:
        """
        The function calculate the conversion rate, standard deviation,
        and standard error for each group and return DataFrame.

        :return: A dataframe with the conversion rate, standard deviation and standard error for each
        group.

        """

        # Calculate the Conversion Rate of Sample and return in percentage for both A & B set
        conv_rt_a = f"{np.mean(self.a_sample[self.response_column]):.2%}"
        conv_rt_b = f"{np.mean(self.b_sample[self.response_column]):.2%}"  

        # Calculate the Standard Deviation and return in percentage for both A & B set
        std_a = f"{np.std(self.a_sample[self.response_column], ddof=0):.3}" 
        std_b = f"{np.std(self.b_sample[self.response_column], ddof=0):.3}"

        # Calculate the Standard Error and return in percentage for both A & B set
        std_err_a = f"{np.std(self.a_sample[self.response_column], ddof=1)/ np.sqrt(np.size(self.a_sample[self.response_column])):.3}"
        std_err_b = f"{np.std(self.b_sample[self.response_column], ddof=1)/ np.sqrt(np.size(self.b_sample[self.response_column])):.3}"
        
        # Create the final report on performance of the set
        conv_rt_report = pandas.DataFrame(data={"Conversion Rate":[conv_rt_a,conv_rt_b],
                                "Standard Deviation":[std_a,std_b],
                                "Standard Error":[std_err_a,std_err_b]},
                                index=[self.a_label,self.b_label]
        )
        
        return conv_rt_report

    def significance_test(self,threshold:float=0.05) -> str:
        """
        It takes the two samples, calculates the number of successes in each sample, and then uses the
        `proportions_ztest` function from the `statsmodels` library to calculate the z-statistic and
        p-value. 
        
        The `proportions_ztest` function also calculates the confidence intervals for each sample, which
        we then return as part of the results
        
        :param threshold: The significance level. Default is 0.05
        :type threshold: int
        :return: The z statistic, p-value, and confidence intervals for both groups.
        """
        # Count the Individual Count all 0's + 1's
        no_of_a = self.a_sample[self.response_column].count()
        no_of_b = self.b_sample[self.response_column].count()
        
        # Count the total Sum of 1's
        successes_of_groups = [self.a_sample[self.response_column].sum(), self.b_sample[self.response_column].sum()]

        # Calculate the Z's and P value using proportion-ztest
        z_stat, pval = proportions_ztest(successes_of_groups, nobs=[no_of_a, no_of_b])

        # Calculate the Confidence level 
        (lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes_of_groups, nobs=[no_of_a, no_of_b], alpha=threshold)
        
        # Check the p-value is lower than threshold or not and draw the conclusion
        if pval > threshold:
            conclusion = (f"\n\nThe Group {self.a_label} fail to perform significantly different than group {self.b_label}."
                          f"\nThe P-Value of the test is {pval:.3f} which is above {threshold}, hence Null hypothesis Hₒ cannot be rejected."
                        )
        else:
            conclusion = (f"\n\nThe Group {self.a_label} able to perform significantly different than group {self.b_label}."
                          f"\nThe P-Value of the test is {pval} which is below {threshold}, hence Null hypothesis Hₒ can be rejected."
                        )
        
        # Pass the Results of the test
        results = ( f"z statistic: {z_stat:.2f}\tp-value: {pval:.3f}"
                    f"\nConfidence Interval 95% for {self.a_label} group: {lower_con:.2%} to {upper_con:.2%}"
                    f"\nConfidence Interval 95% for {self.b_label} group: {lower_treat:.2%} to {upper_treat:.2%}")+ conclusion

        return results