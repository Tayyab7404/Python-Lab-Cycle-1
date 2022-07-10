# Bitwise operators

n1 = int(input("Enter first number: "))

n2 = int(input("Enter second number: "))

print(n1,"in Binary = ",bin(n1).replace('0b',''))
print(n2,"in Binary = ",bin(n2).replace('0b',''))

print("BITWISE OPERATIONS")

print(bin(n1).replace('0b','')," | ",bin(n2).replace('0b','')," = ",n1|n2)

print(bin(n1).replace('0b','')," & ",bin(n2).replace('0b','')," = ",n1&n2)

print("~ ",bin(n1).replace('0b','')," = ",~n1)

print("~ ",bin(n2).replace('0b','')," = ",~n2)

print(bin(n1).replace('0b','')," ^ ",bin(n2).replace('0b','')," = ",n1^n2)

print(bin(n1).replace('0b','')," >> 2 = ",n1>>2)

print(bin(n1).replace('0b','')," << 2 = ",n1<<2)

print(bin(n2).replace('0b','')," >> 2 = ",n2>>2)

print(bin(n2).replace('0b','')," << 2 = ",n2<<2)
