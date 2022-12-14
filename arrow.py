n = int(input("ENTER NUMBER OF COLUMNS: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(n-i+j-1, end=' ')
    print()

for i in range(1, n):
    for j in range(1, n-i+1):
        print(i+j-1, end=' ')
    print()