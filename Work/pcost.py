# pcost.py
#
# Exercise 1.27

import csv
import report

def portfolio_cost(file_name):
    '''
    Computes the total cost (shares*price) of a portfolio file.
    '''
    portfolio = report.read_portfolio(file_name)
    return sum([s['shares'] * s['price'] for s in portfolio])

# filename = input('Enter the full path of your file: ')
# cost = portfolio_cost(filename)
# print('Total cost:', cost)