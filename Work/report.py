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
        rows = csv.reader(file)
        head = next(rows)
        for row in rows:
            record = dict(zip(head, row))
            dic = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])}
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

def make_report(portfolio: list, prices: dict) -> list:
    '''
    Takes a list of stocks and dictionary of prices as input and returns a list of tuples containing the Name, Shares, Price and Change.
    '''
    res = []
    for l in portfolio:
        current_price = prices[l['name']]
        previous_price = l['price']
        change = current_price - previous_price
        line = [l['name'], l['shares'], current_price, change]
        res.append(tuple(line))

    return res

def print_report(report: list):
    '''
    Take a list contains the name, shares, price, change, and output a beautiful chart.
    '''

    # output a chart
    headers = ('Name', 'Shares', 'Price', 'Change')
    a, b, c, d = headers
    print(f'{a:>10s} {b:>10s} {c:>10s} {d:>10s}')

    print(f"{'':->10s} {'':->10s} {'':->10s} {'':->10s}")

    for a, b, c, d in report:
        price_str = f'${c:.2f}'
        print(f'{a:>10s} {b:>10d} {price_str:>10s} {d:>10.2f}')

    return

def portfolio_report(path1: str, path2: str):
    '''
    Take 2 paths as input, and output a chart describing the portfolios.
    '''
    portfolio = read_portfolio(path1)
    price = read_prices(path2)
    report = make_report(portfolio, price)
    print_report(report)
    
    return