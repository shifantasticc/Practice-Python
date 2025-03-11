#Even and Odd number
x = int(input("enter a number:"))

if x%2 == 0:
    print(x, "is positive")
elif x%2 == 1:
    print(x, "is negative")
else:
    print("Invalid entry")

#Greater num
a = int(input("enter a number:"))
b = int(input("enter a number:"))

if a>b:
    print(a,"is greater")
elif b>a:
    print(b,"is greater")
else:
    print("both are equal")