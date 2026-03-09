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
            tup = (l[0], float(l[1]), float(l[2]))
            res.append(tup)

    return res