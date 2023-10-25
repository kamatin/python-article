# left pascal triangle
n = int(input("enter the num:"))
for i in range(n):
    
    for j in range(n - i-1):
        print(' ', end='')
    
    for k in range(i + 1):
        print('*', end='')
    print()
for i in range(n):
    
    for j in range(i + 1):
        print(' ', end='')

    for k in range(n - i-1):
        print('*', end='')
    print()

# right pascal traingle:
for i in range(n):
    for j in range(i + 1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    print()

# left triangle

for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()

# right triangle


for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()



# pyramid

for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

# reverse pyramid

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(n-i)+1):
        print("*",end="")
    print()



#reverse pyramid2


for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(n-i)+1):
        print("*",end="")
    print()

    
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

    









    
    
