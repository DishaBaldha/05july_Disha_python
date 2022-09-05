from decimal import *
data = list(map(Decimal, '12.50 25.69 27.45 39.45 21.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))