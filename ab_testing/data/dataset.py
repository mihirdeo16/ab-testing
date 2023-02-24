import pandas
import numpy
import random
import random, string


# A Dataset is a collection of data points, each of which is a collection of features.
class Dataset:
    def __init__(self, number_of_users=1000,prob_a=[0.60,0.40],prob_b=[0.80,0.20]) -> None:
        """
        > The function `__init__` initializes the class `ABTest` with the number of users, the probability
        of being in group A, and the probability of being in group B
        
        :param number_of_users: The number of users we want to simulate, defaults to 1000 (optional)
        :param prob_a: The probability of 0 & 1 in group A
        :param prob_b: The probability of 0 & 1 in group B
        """


        self.number_of_users = number_of_users
        self.B = None
        self.A = None
        self.df = None
        self.prob_a = prob_a
        self.prob_b = prob_b

    def generate_data(self,group,probability) -> pandas.DataFrame:
        """
        It generates a dataframe with a column of users, a column of responses, and a column of groups
        
        :param group: The name of the group
        :param probability: The probability of a user responding to the treatment
        :return: A dataframe with the columns Users, Response, and Group.
        """
        users = [
            "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
            for i in range(0, self.number_of_users)
        ]

        response = numpy.random.choice(
            [0, 1], size=(self.number_of_users), p=probability
        )

        df = pandas.DataFrame(
            data={"Users": users, "Response": response,"Group":group}
        )
        return df
    
    def data(self) -> pandas.DataFrame:
        """
        > The function generates two groups of data, A and B, and then concatenates them together into a
        single dataframe
        :return: A dataframe with the data
        """
        # Set the 1 and 0 probability as 60-40 %
        self.A = self.generate_data(group="A",probability=self.prob_a)

        # Set the 1 and 0 probability as 80-20 %
        self.B = self.generate_data(group="B",probability=self.prob_b)

        # Concat the dataframe
        self.df = pandas.concat([self.A,self.B])

        # Shuffle the data
        self.df = self.df.sample(frac=1).reset_index(drop=True)

        return self.df
