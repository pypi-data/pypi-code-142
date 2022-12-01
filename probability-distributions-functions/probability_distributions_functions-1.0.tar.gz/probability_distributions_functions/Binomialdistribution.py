import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials


    A binomial distribution is defined by two variables:
        the probability of getting a positive outcome
        the number of trials
    
    If you know these two values, you can calculate the mean and the standard deviation.        
    """
    
    def __init__(self,prob=.5, size=20):
    
        """
        Stores the probability of the distribution in an instance variable p.
        Stores the size of the distribution in an instance variable n.
        Now that we know p and n, you can calculate the mean and standard deviation.
        Then use the init function from the Distribution class to initialize the
        mean and the standard deviation of the distribution.
        """

        self.p = prob
        self.n = size
        Distribution.__init__(self,self.calculate_mean(), self.calculate_stdev())
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
        

        Calculates the mean of the Binomial distribution. Stores the mean
        via the self variable and also return the new mean value
        """
                
        self.mean= self.p*self.n
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
        
        Calculates the standard deviation of the Binomial distribution. Stores
        the result in the self variable then returns the value of the standard deviation.
        """

        self.stdev=math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
        
        The read_data_file() from the Generaldistribution class can read in a data file.
        However, the method doesn't update the mean or standard deviation of a distribution.
        Hence this method calculates the n, p, mean and standard deviation from a data set and then updates the n, p, mean and stdev attributes.
        Assume that the data is a list of zeros and ones like [0 1 0 1 1 0 1]. 

        updates the n attribute of the binomial distribution
        updates the p value of the binomial distribution by calculating the
        number of positive trials divided by the total trials
        updates the mean attribute
        updates the standard deviation attribute
        """        
               
        self.n=len(self.data)
        self.p=float((self.data.count(1)/len(self.data)))
        self.mean=self.calculate_mean()
        self.stdev=self.calculate_stdev()
        return (self.p,self.n)
        
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        plt.bar(x = ['0', '1'], height = (self.data.count(0),self.data.count(1)))
        #plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.xlabel('Zero or One')
        plt.ylabel('Results of each case')
        plt.title('Bar chart of head or tails')
        plt.show()
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output


        Calculate the probability density function for a binomial distribution.
        For a binomial distribution with n trials and probability p, 
        the probability density function calculates the likelihood of getting k positive outcomes. 
        """
        return ((math.factorial(self.n)/(math.factorial(k)*math.factorial(self.n-k)))*pow(self.p,k)*pow((1.0-self.p),self.n-k))        

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        x=[]
        y=[]
        for i in range(self.n+1):
            y.append(self.pdf(i))
            x.append(i)
        plt.bar(x,y)
        plt.xlabel('Probability distributions')
        plt.ylabel('Probability')
        plt.title('Probability outcome')
        plt.show()
        return(x,y)
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            

        Define addition for two binomial distributions. Assume that the
        p values of the two distributions are the same. The formula for 
        summing two binomial distributions with different p values is a little complicated,
        so it's going to be implmented in future works.
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
             
        result=Binomial()
        result.n=self.n+other.n
        result.p=self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """

        return "mean {},standard deviation {}, p {}, n {}".format(self.mean,self.stdev,self.p,self.n)
