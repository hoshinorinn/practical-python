# mortgage.py
#
# Exercise 1.7

principal = 500000
monthly_payment = 2684.11
interest_rate = 0.05
total_paid = 0
month = 1
extra_payment_start_month = int(input('extra payment start month: '))
extra_payment_end_month = int(input('extra payment end month: '))
extra_payment = int(input('extra payment: '))

while((principal > 0) and (month < extra_payment_start_month)):
    principal = principal * (1 + interest_rate/12) - monthly_payment
    month += 1
    total_paid += monthly_payment
    print(round(total_paid, ndigits=4), round(principal, ndigits=4))

while((month >= extra_payment_start_month) and (month <= extra_payment_end_month)):
    principal = principal * (1 + interest_rate/12) - (monthly_payment + extra_payment)
    month += 1
    total_paid += (monthly_payment + extra_payment)
    print(round(total_paid, ndigits=4), round(principal, ndigits=4))

while(principal > 0):
    if((principal * (1 + interest_rate/12)) < monthly_payment):
        total_paid += principal * (1 + interest_rate/12)
        month += 1
        principal = 0
        print(round(total_paid, ndigits=4), round(principal, ndigits=4))
        break
    principal = principal * (1 + interest_rate/12) - monthly_payment
    month += 1
    total_paid += monthly_payment
    print(round(total_paid, ndigits=4), round(principal, ndigits=4))

print('Total paid:', total_paid)
print('Months required:', month-1)