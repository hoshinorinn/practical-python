# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(file_name):
    '''
    Reads the portfolio data, and returns the total cost of the portfolio as a float.
    '''
    total_cost = 0
    with open(f'{file_name}', 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, line in enumerate(rows):
            record = dict(zip(headers, line))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {i+1}: Couldn\'t convert: {line}')
                pass
    print('Total cost:', total_cost)
    return

# portfolio_cost('D:\\practical-python\\Work\\Data\\missing.csv')
portfolio_cost(r'D:\practical-python\Work\Data\portfoliodate.csv')