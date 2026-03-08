# pcost.py
#
# Exercise 1.27

cost = 0

with open(r'D:\practical-python\Work\Data\portfolio.csv', 'r') as f:
    next(f) # skip the head line of the file
    for line in f:
        l = line.split(',')
        cost += float(l[1]) * float(l[2])

print('Total cost', cost)