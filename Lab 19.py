t = (7, 21, 23, 25, 27, 29,)
print("Before inserting the elements of the tuple are: ", t)

x = int(input("Enter the element to insert in the tuple: "))
pos = int(input("Enter the position to insert the element: "))

t = t[:pos-1] + (x, ) + t[pos-1:]
print("After the inserting the elements of the tuple are: ", t)
