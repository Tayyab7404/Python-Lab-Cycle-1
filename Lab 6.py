# Menu Driven Program to find the properties of numbers

def fact(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact * i
    return fact

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def isArmstrong(n):
    l = len(str(n))
    sum = 0
    for i in str(n):
        sum = sum + int(i)**l
    if sum == n:
        return True
    else:
        return False

def isStrong(n):
    sum = 0
    for i in str(n):
        sum = sum + fact(int(i))
    if sum == n:
        return True
    else:
        return False

def isPerfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum = sum + i
    if sum == n:
        print(n," is a Perfect number")
    elif sum > n:
        print(n," is an Abundant number")
    else:
        print(n," is a Deficient number")
        
n = int(input("Enter a number: "))

while True:
    print("\nMENU")
    print("----")
    print("1.Prime")
    print("2.Armstrong")
    print("3.Strong")
    print("4.Perfect")
    print("5.Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        if isPrime(n):
            print(n," is a Prime number")
        else:
            print(n," is a Composite number")
            
    elif ch == 2:
        if isArmstrong(n):
            print(n," is an Armstrong number")
        else:
            print(n," is not an Armstrong number")
        
    elif ch == 3:
        if isStrong(n):
            print(n," is a Strong number")
        else:
            print(n," is not a Strong number")
        
    elif ch == 4:
        isPerfect(n)

    elif ch == 5:
        break
    else:
        print("Invalid input")
