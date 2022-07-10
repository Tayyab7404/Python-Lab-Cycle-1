def perm(a, end=[]):
    if len(a) == 0:
        print(end)
    else:
        for i in range(len(a)):
            perm(a[:i] + a[i+1:], end+a[i:i+1])


a = [int(i) for i in input('Enter space separated values: ').split()]

print("Given list is: ", a)

a.sort()
print('After sorting, the list is: ', a)

x = int(input("Enter a number to search in the list: "))
if x in a:
    print(x, " is present in the list")
else:
    print(x, " is not present in the list")

print("All possible permutations of the list: ")
perm(a)
