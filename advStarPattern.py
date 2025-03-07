#left slash pattern
for i in range(1,5):
    for j in range(1,8):
        if j==i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()
#pyramid pattern
for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#number pyramid pattern
p=1
for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print(p,end='')
            p=p+1
        else:
            print(" ",end='')
    print()
    p=1
