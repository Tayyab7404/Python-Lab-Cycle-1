from math import *

def ncr(n, r):
    return int(factorial(n)/(factorial(n-r) * factorial(r)))


n = int(input("Enter no of rows: "))
for i in range(0, n):
    for j in range(1, n-i+1):
        print(end='  ')
    for j in range(0, i+1):
        print(str(ncr(i, j)).rjust(2), end='  ')
    print()
