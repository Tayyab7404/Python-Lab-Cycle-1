def GCD(x,y):
        return y if x%y==0 else GCD(y,x%y)
    
def factorial(n):
        return 1 if n <= 1 else n*factorial(n-1)
    
def fib(a):
        return a if a <= 1 else fib(a - 1) + fib(a - 2)
    
def TOH(n, l, r, c):
    if n > 0:
        TOH(n-1, l, c, r)
        print("Move disk ", n, "from ", l, "to ", r)
        TOH(n-1, c, r, l)


print("GCD:")
x = int(input("Enter the first number :"))
y = int(input("Enter the second number :"))
print("The GCD of ",x," and ",y," is:",GCD(x,y))


print("\nFibonacci:")
n = int(input('Enter number of numbers to generate: '))
for i in range(0, n+1):
    print(fib(i), end=' ')


print("\n\nFactorial:")
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: ", factorial(n))


print("\nTowers of Hanoi:")
n = int(input("Enter number of disks: "))
TOH(n, 'L', 'R', 'C')
