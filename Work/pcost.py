# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(file_name):
    '''
    Reads the portfolio data, and returns the total cost of the portfolio as a float.
    '''
    cost = 0
    fail = 0
    with open(f'{file_name}', 'r') as f:
        next(f)
        rows = csv.reader(f)
        for i, line in enumerate(rows):
            try:
                # l = line.split(',')
                cost += float(line[1]) * float(line[2])
            except ValueError:
                fail +=1
                print(f'Row {i+1}: Couldn\'t convert: {line}')
                pass
    return cost

# cost = portfolio_cost('D:\\practical-python\\Work\\Data\\portfolio.csv')
cost = portfolio_cost('D:\\practical-python\\Work\\Data\\missing.csv')
print('Total cost:', cost)