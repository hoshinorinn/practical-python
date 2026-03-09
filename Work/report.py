# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''
    Read the portfolio file and return a list of tuples containing the contents of the file.
    '''
    res = []

    with open(f'{filename}', 'r') as file:
        next(file)
        for line in file:
            l = line.split(',')
            dic = {'name': l[0], 'shares': float(l[1]), 'price': float(l[2])}
            res.append(dic)

    return res

def read_prices(filename):
    '''
    Read the name-price file into a dictionary.
    '''
    res = {}

    with open(filename, 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                res[f'{row[0]}'] = float(row[1])
            except (ValueError, IndexError):
                print('Oops, there may be a blank line in your file... check it!')
                pass

    return res