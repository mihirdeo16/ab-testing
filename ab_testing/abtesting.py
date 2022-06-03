
import pandas 

class ABTest:

    def __init__(self,df_A:pandas.DataFrame,response_column:str, df_B:pandas.DataFrame=None,group_column:str=None,labels = ['A','B']):
        """
        The function takes in two dataframes, one for each group, and a column name for the response
        variable. It then creates a new object with attributes for the two dataframes, the response
        variable, and the group labels
        
        :param df_A: The first dataframe
        :type df_A: pandas.DataFrame
        :param response_column: The column name of the response variable
        :type response_column: str
        :param df_B: The second dataframe
        :type df_B: pandas.DataFrame
        :param group_column: The column name that indicates the group
        :type group_column: str
        :param labels: The labels for the two groups
        """
        
        self.response_column = response_column

        if group_column !=None:
            self.group_column = group_column
            if df_A[self.group_column].nunique() !=2:
                ValueError('Group column should contain two distinct values')

            self.groups_ele = list(df_A[self.group_column].unique())

            self.a_sample = df_A[self.group_column==self.groups_ele[0]]
            self.b_sample  = df_A[self.group_column==self.groups_ele[2]]

        elif df_B !=None:
            self.b_sample = df_B
            self.a_sample = df_A


        elif df_B ==None and group_column==None:
            ValueError('Either provide the df_B or give column name for group indication')

        self.a_label = labels[0]
        self.b_label = labels[1]

    def info(self):
        pass        
    def report(self):
        pass
