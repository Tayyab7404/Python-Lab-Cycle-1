# Desktop Calculator

n1 = int(input("Enter first number: "))

x = input("Enter the operator(+, -, *, /, **, //, %): ")

n2 = int(input("Enter second number: "))

if x == '+':
    print(n1,x,n2," = ",n1+n2)
    
elif x == '-':
    print(n1,x,n2," = ",n1-n2)
    
elif x == '*':
    print(n1,x,n2," = ",n1*n2)
    
elif x == '**':
    print(n1,x,n2," = ",n1**n2)

elif x == '/':
    print(n1,x,n2," = ",n1/n2)

elif x == '//':
    print(n1,x,n2," = ",n1//n2)

elif x == '%':
    print(n1,x,n2," = ",n1%n2)

else:
    print("Invalid Operator")
