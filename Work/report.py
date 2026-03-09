# report.py
#
# Exercise 2.4

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