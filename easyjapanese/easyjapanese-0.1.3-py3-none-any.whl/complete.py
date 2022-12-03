import traceback
import datetime

import pandas as pd


class Complete():
    """This class completes the whole process of web scraping.

    So far, I define the methods for obtaining the date of the retrieved easy 
    news data and creating a dataframe from the retireved datas. If there is
    a need for another manipulations related to this whole scraping processes,
    then a code for the manipulations will be added here.

    Attributes
    ----------
    easy_urls : list
        A list of the NEWS WEB EASY URLs.
    easy_articles : list
        A list of the body text of NEWS WEB EASY articles.
    regular_urls : list
        A list of the NEWS WEB URLs.
    regular_articles : list
        A list of the body text of NEWS WEB articles.
    date : str
        Date of the newly retrieved data
    SAVE_PATH : str
        The filepath of the directory where you want to save all the retrieved data.
    df_old : pandas.core.frame.DataFrame
        A pandas dataframe that you want to concatenate your new data with.
    df : pandas.core.frame.DataFrame
        The pandas dataframe that you make from the retrieved data.
    df_piled : pandas.core.frame.DataFrame
        A pandas dataframe that you concatenate df with df_old.
    date_new : datetime.datetime
        The date of the newly retrieved data.
    """
    def __init__(self, easy_urls, easy_articles,
                regular_urls, regular_articles, date):
        """Constructor.
        Define the attributes mainly for creating the data frame.
        """
        self.easy_urls = easy_urls
        self.easy_articles = easy_articles
        self.regular_urls = regular_urls
        self.regular_articles = regular_articles
        self.date = date
        SAVE_PATH = input('The filepath, where you want to save the final output data?')
        self.SAVE_PATH = SAVE_PATH
        self.df_old = pd.read_csv(self.SAVE_PATH)
        

    def make_df(self):
        """Create the dataframe from the retrieved data.
        """
        # length_test didn't work well, so 
        # self.input_length_test()
        try:    
            new_date = self.get_date()
        except:
            print('An expected error has occurred during get_date().')
            traceback.print_exc()
        try:
            self.df = pd.DataFrame({
                'Date': new_date,
                'Easy URL': self.easy_urls,
                'Easy article': self.easy_articles,
                'Regular URL': self.regular_urls,
                'Regular article': self.regular_articles
            })
        except:
            print('An expected error has occurred during making a df.')
            traceback.print_exc()
        
        
    def concat(self):
        """Pile up the created dataframe on the existing dataframe and save it.
        """
        try:
            self.df_piled = pd.concat([self.df, self.df_old])
            self.df_piled['Date'] = pd.to_datetime(self.df_piled['Date'])
            self.df_piled.to_csv(self.SAVE_PATH, index=False)
        except:
            print('An expected error has occurred during concat().')
            traceback.print_exc()
            self.df_piled = 'Unexpected'
        return self.df_piled
    

    
    # def input_length_test(self):
    #     """(Soon to be deleted) Check if the retrieved datas have unequal shape.
    #     """
    #     try:
    #         if ~(
    #             len(self.easy_urls) == len(self.easy_articles)\
    #             == len(self.regular_urls) == len(self.regular_articles)
    #         ):
    #             raise LengthError('An unexpected error has occured with some or all of the four inputs.')
    #     except LengthError:
    #         print(traceback.print_exc())

    def get_date(self):
        """Obtain the date of newly retrieded data.
        """
        old_date = datetime.datetime.strptime(
            self.df_old['Date'][0], '%Y-%m-%d'
            )
        new_date_raw = datetime.datetime.strptime(
                self.date, '%m月%d日'
                )
        if (old_date.month==12) & (new_date_raw.month==1):
            new_year = old_date.year + 1
        else:
            new_year = old_date.year
        self.date_new = datetime.datetime(
                new_year, new_date_raw.month, new_date_raw.day
                )
        return self.date_new



# class LengthError(Exception):
#     """This error notifies the unequal length of the inputs; URLs and articles.
#     """
#     pass