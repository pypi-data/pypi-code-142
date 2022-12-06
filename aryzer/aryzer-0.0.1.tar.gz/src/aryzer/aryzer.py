import os

import matplotlib.pyplot as plt


def get_larger_than_percentile(dataframe, percentile):
    return dataframe[dataframe.rank(pct=True) > percentile].sort_values(ascending=False)


def create_overview_of_categories(dataframe):
    for percentage in [50, 75, 95]:
        largest = get_larger_than_percentile(dataframe, percentage / 100)
        print(largest)
        largest.plot.bar()
        save_plot('categories_largest_' + str(percentage) + '_percentile')


def save_plot(plot_name):
    result_dir = os.path.abspath('../results/')
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    plt.savefig(fname=os.path.join(result_dir, plot_name + '.png'), dpi='figure', format='png')