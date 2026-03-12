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
    cost = sum([s['shares'] * s['price'] for s in portfolio])
    print('Total cost:', cost)
    return cost

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile' % args[0])
    portfolio_cost(args[1])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)