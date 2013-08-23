import sys


def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

print (gcd(int(sys.argv[1]), int(sys.argv[2])))