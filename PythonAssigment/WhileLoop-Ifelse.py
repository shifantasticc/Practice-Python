# Q.4
numbers = [1, 3, 5, 7, 9, 11, 13]
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        print('There are Even Numbers in the list')
        break
    i += 1
else:
    print('There are no Even Numbers in the list')
