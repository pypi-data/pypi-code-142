"""
Generates performance reports for your stock portfolio.
"""
import datetime
from collections import OrderedDict
import argparse
import csv
import requests


def main(args=None):
    """
    Entrypoint into program.
    """
    args = get_args(args)
    portfolio_list = read_portfolio(args.source)
    symb_list = []
    units_dict = {}
    cost_dict = {}
    for i in portfolio_list:
        for key in i.keys():
            if key=='symbol' and i[key] not in symb_list:
                symb_list.append(i[key])
                units_dict.update({i[key]: i['units']})
                cost_dict.update({i[key]: i['cost']})
            break
    market_data = get_market_data(symb_list)
    metrics_list = calculate_metrics(units_dict, cost_dict,
    market_data[0], market_data[1], market_data[2])
    save_portfolio(metrics_list, args.target)

def read_portfolio(filename):
    """
    Returns data from a CSV file
    """
    portfolio_data = []
    with open(filename, newline='', encoding="utf-8") as file:
        portfolio_reader = csv.DictReader(file)
        for row in portfolio_reader:
            data_list = [('symbol', row['symbol']), ('units', row['units']), ('cost', row['cost'])]
            portfolio_data.append(OrderedDict(data_list))
    return portfolio_data

def get_args(args=None):
    """
    Parse and return command line argument values
    """
    input_file = 'portfolio.csv'
    output_file = 'portfolio_output.csv'
    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
    help="enter portfolio filename here", default=input_file)
    parser.add_argument('--target',
    help="enter portfolio report filename here", default=output_file)
    return parser.parse_args(args)

def get_market_data(stocks_list):
    """
    Get the latest market data for the given stock symbols
    """
    symbols_join = ','.join(stocks_list)
    portfolio_rqst = requests.get(f'https://cloud.iexapis.com/stable/tops/last?token=pk_218d34d32a4346b78a2a2b880fff971b&symbols={symbols_join}')
    portfolio_data = portfolio_rqst.json()
    stocks_list_found = []
    stocks_not_found = []
    stock_prices_dict = {}
    for stock in portfolio_data:
        stocks_list_found.append(stock['symbol'])
        stock_prices_dict.update({stock['symbol']: stock['price']})
    for stock in stocks_list:
        if stock not in stocks_list_found:
            stocks_not_found.append(stock)
    return stocks_list_found, stock_prices_dict, stocks_not_found

def calculate_metrics(portfolio_units, portfolio_cost, iex_stocks_found, iex_prices, iex_stocks_not_found):
    """
    Calculates the various metrics of each of the stocks
    """
    metrics_data = []
    for found_stocks in iex_stocks_found:
        book_value = (int(portfolio_units[found_stocks])*float(portfolio_cost[found_stocks]))*100
        market_value = int((iex_prices[found_stocks]
        *float(portfolio_units[found_stocks]))*100)
        gain_loss = market_value -book_value
        change = round(gain_loss/book_value,3)
        data_list = [('symbol', found_stocks), ('units', portfolio_units[found_stocks]), ('cost', portfolio_cost[found_stocks]),
        ('latest_price', iex_prices[found_stocks]), ('book_value', book_value), ('market_value', market_value), ('gain_loss', gain_loss), ('change', change)]
        metrics_data.append(OrderedDict(data_list))
    metrics_data.append(iex_stocks_not_found)
    return metrics_data

def save_portfolio(metrics_data, filename):
    """
    Saves data to a CSV file
    """
    data_to_write = []
    temp_dict = {}
    if isinstance(metrics_data,list) and len(metrics_data)==1:
        index_val = 0
    else:
        index_val = -1
    for data_index in range(0,len(metrics_data)+index_val):
        temp_dict=({'symbol': metrics_data[data_index]['symbol'], 'units': metrics_data[data_index]['units'],
        'cost': metrics_data[data_index]['cost'], 'latest_price': metrics_data[data_index]['latest_price'],
        'book_value': metrics_data[data_index]['book_value'], 'market_value': metrics_data[data_index]['market_value'],
        'gain_loss': metrics_data[data_index]['gain_loss'], 'change': metrics_data[data_index]['change']})
        data_to_write.append(temp_dict)
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, ['symbol', 'units', 'cost', 'latest_price',
        'book_value', 'market_value', 'gain_loss', 'change'])
        writer.writeheader()
        writer.writerows(data_to_write)
        writer = csv.writer(file)
        stocks_not_found = metrics_data[len(metrics_data)-1]
        if isinstance(stocks_not_found,list):
            writer.writerow({''})
            writer.writerow({'WARNING: Stock symbols below were not found at IEX.'})
            for i in range(0,len(stocks_not_found)):
                writer.writerow({stocks_not_found[i]})
            writer.writerow({''})
            writer.writerow({f'time stamp: {datetime.datetime.now()}'})
    return data_to_write


if __name__ == '__main__':
    main()
