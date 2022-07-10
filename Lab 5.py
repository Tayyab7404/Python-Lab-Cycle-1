# Number of days in a month

def isLeap(n):
    if n%400 == 0 or (n%100 != 0 and n%4 == 0):
        return True
    else:
        return False

mm = int(input("Enter the month: "))
yy = int(input("Enter the year: "))


if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    print("31 days")
elif mm == 2:
    if isLeap(yy):
            print("29 days")
    else:
            print("28 days")
else:
        print("30 days")


