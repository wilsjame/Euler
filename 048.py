"""
brute force series 1^2 + 2^2 + 3^3 + ... + 1000^1000
print last ten digits
"""
n: int  = 0
for i in range(1, 1001):
    n += i**i
print(str(n)[-10:])
