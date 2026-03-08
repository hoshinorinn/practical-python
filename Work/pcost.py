# pcost.py
#
# Exercise 1.27

def portfolio_cost(file_name):
    '''
    Reads the portfolio data, and returns the total cost of the portfolio as a float.
    '''
    cost = 0
    fail = 0
    with open(f'{file_name}', 'r') as f:
        next(f)
        for line in f:
            try:
                l = line.split(',')
                cost += float(l[1]) * float(l[2])
            except ValueError:
                fail +=1
                print(f'{fail} line(s) failed, total cost can be wrong, check your file!')
                pass
    return cost

# cost = portfolio_cost('D:\\practical-python\\Work\\Data\\portfolio.csv')
cost = portfolio_cost('D:\\practical-python\\Work\\Data\\missing.csv')
print('Total cost:', cost)