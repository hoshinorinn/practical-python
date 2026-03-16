# report.py
#
# Exercise 2.4

import csv
import fileparse
from stock import Stock
import tableformat

def read_portfolio(filename):
    '''
    Read the portfolio file and return a list of tuples containing the contents of the file.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
    
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):
    '''
    Read the name-price file into a dictionary.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

def make_report(portfolio: list, prices: dict) -> list:
    '''
    Takes a list of stocks and dictionary of prices as input and returns a list of tuples containing the Name, Shares, Price and Change.
    '''
    res = []
    for l in portfolio:
        current_price = prices[l.name]
        previous_price = l.price
        change = current_price - previous_price
        line = [l.name, l.shares, current_price, change]
        res.append(tuple(line))

    return res

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)