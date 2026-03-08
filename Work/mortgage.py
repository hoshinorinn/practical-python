# mortgage.py
#
# Exercise 1.7

principal = 500000
monthly_payment = 2684.11
interest_rate = 0.05
total_paid = 0
month = 0

for i in range(12):
    principal = principal * (1 + interest_rate/12) - monthly_payment - 1000
    month += 1
    total_paid += (monthly_payment + 1000)

while(principal > 0):
    principal = principal * (1 + interest_rate/12) - monthly_payment
    month += 1
    total_paid += monthly_payment

print('Total paid', total_paid)
print('Months required', month)