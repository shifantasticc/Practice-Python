'''for i in range(4):
    print("A",end='')
    for j in range(3):
        print("B",end='')
    print()'''

#5x5 star pattern
for i in range(3):
    for j in range(3):
        print("*",end='')
    print()

#left lower triangle pattern
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
print()
#right upper triangle pattern
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()
#left upper triangle pattern
for i in range(1,6):
    for j in range(1,6):
        if j<=6-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()
#right lower triangle pattern
for i in range(1,6):
    for j in range(1,6):
        if j>=6-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()


print()

