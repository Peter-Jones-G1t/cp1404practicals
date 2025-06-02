for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c. Print n stars
n = int(input("Enter number: "))
for i in range(n):
    print('*', end=' ')
print()

#d. print n lines of increasing stars
n = int(input("Enter number: "))
for i in range(1, n + 1):
    print('*' * i)
