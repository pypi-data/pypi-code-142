""" Main-File to train classifier """

import os

import matplotlib.pyplot as plt


def filter_df_by_percentile(dataframe, percentile):
    """ filter dataframe by percentile """
    return dataframe[dataframe.rank(pct=True) > percentile].sort_values(ascending=False)


def filter_df_by_category(dataframe, category):
    """ filter dataframe by category """
    return dataframe[category in dataframe['labels']]


def create_overview_of_categories(dataframe):
    """ filter a dataframe by 50%, 75%, 95% percentiles and save it in the results folder """
    for percentage in [50, 75, 95]:
        largest = filter_df_by_percentile(dataframe, percentage / 100)
        print(largest)
        largest.plot.bar()
        save_plot('categories_largest_' + str(percentage) + '_percentile')


def save_plot(plot_name):
    """ saves the result of a plot in a file in the results folder """
    result_dir = os.path.abspath('../results/')
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    plt.savefig(fname=os.path.join(result_dir, plot_name + '.png'), dpi='figure', format='png')
