# kieran hulsman
# pi-gen project
# july 11
# testing the BBP pi formula
from decimal import *
getcontext().prec = 1000 # sets precision

def summand (k) -> Decimal:
    a = Decimal(1) / Decimal(16 ** k)
    b = Decimal(4) / Decimal(8*k + 1)
    c = Decimal(2) / Decimal(8*k + 4)
    d = Decimal(1) / Decimal(8*k + 5)
    e = Decimal(1) / Decimal(8*k + 6)
    return a * (b - c - d - e)

def summation (upper_bound):
    res = Decimal(0)
    for i in range (0, upper_bound+1):
        res += summand(i)
    return res

print(summation(10))