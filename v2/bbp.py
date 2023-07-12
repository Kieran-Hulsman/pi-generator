# kieran hulsman
# pi-gen project
# july 11
# testing the BBP pi formula
from decimal import *
DIGITS = 10000000
getcontext().prec = DIGITS + 100 # sets precision

def summand (k) -> Decimal:
    a = Decimal(1) / Decimal(16 ** k)
    b = Decimal(4) / Decimal(8*k + 1)
    c = Decimal(2) / Decimal(8*k + 4)
    d = Decimal(1) / Decimal(8*k + 5)
    e = Decimal(1) / Decimal(8*k + 6)
    return a * (b - c - d - e)

def summation (upper_bound):
    prev = Decimal(0)
    cur = prev
    for i in range (0, upper_bound):
        cur += summand(i)
        if cur - prev < Decimal(1) / Decimal(DIGITS+10): return cur
        prev = cur
        # print("{}: {}".format(i, cur - prev))
    return -1

print(summation(100))