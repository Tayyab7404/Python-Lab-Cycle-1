# Roots of a Quadratic Equation

import math

print('Roots of a Quadratic Equation')

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = (b*b)-(4*a*c)

if d==0:
    print('\nRoots are real and identical')
    root1 = root2 = -b/(2*a)
    print('\nRoot 1 = ',root1)
    print('Root 2 = ',root2)
    
elif d>0:
    print('\nRoots are real and distinct')
    root1 = (-b+d**(0.5))/(2*a)
    root2 = (-b-d**(0.5))/(2*a)
    print('\nRoot 1 = ',root1)
    print('Root 2 = ',root2)

else:
    print('\nRoots are imaginary')
    root1 = root2 = (-b/(2*a))
    imaginary = math.sqrt(-d)/(2*a)
    print('\nRoot 1 = ',root1,'+',imaginary,'j')
    print('Root 2 = ',root2,'-',imaginary,'j')

