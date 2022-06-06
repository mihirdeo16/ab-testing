import pandas 
import numpy
import random
import random, string

class Dataset:
    def __init__(self, number_of_users=1000) -> None:

        """
        This function initializes the class with a default number of users of 1000
        
        :param number_of_users: The number of users to generate, defaults to 1000 (optional)
        """

        self.number_of_users = number_of_users
        self.users = None
        self.response = None
        self.df = None

    def data(self) -> pandas.DataFrame:
        """
        > The function creates a dataframe with a column of users, a column of responses, and a column
        of groups
        :return: A dataframe with the following columns: Users, Response, Group
        """

        self.users = [''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) for i in range(0,self.number_of_users)]
        
        self.response  = numpy.random.choice([0, 1], size=(self.number_of_users ), p=[0.80, 0.20])

        self.df = pandas.DataFrame(data={'Users':self.users,
                                    'Response':self.response}
                                    )
        
        l = len(self.df.index) // 2 
        self.df.loc[:l, 'Group'] = 'A'
        self.df.loc[l:, 'Group'] = 'B'

        return self.df