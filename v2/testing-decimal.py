# kieran hulsman
# pi-gen project
# july 11
# testing out precision with decimal lib
from decimal import *
getcontext().prec = 1000
one_seventh = Decimal(1) / Decimal(7)
print(one_seventh * Decimal(7)) # seems to work?