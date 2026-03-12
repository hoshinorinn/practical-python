# report.py
#
# Exercise 2.4

import csv
import fileparse

def read_portfolio(filename):
    '''
    Read the portfolio file and return a list of tuples containing the contents of the file.
    '''
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''
    Read the name-price file into a dictionary.
    '''
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

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

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)