# bounce.py
#
# Exercise 1.5

initial_height = 100
bounce = 3/5

for i in range(10):
    height = round(bounce*initial_height, ndigits=4)
    print(i+1, height)
    initial_height = height