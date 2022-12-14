n = int(input("ENTER NUMBER OF ROWS: "))
for i in range(1, n+1):
    for j in range(0, n-i):
        print(" ", end='')
    c = chr(n+65-i)
    for j in range(i):
        print(c, end=' ')
        c = chr(ord(c)+1)
    print()
for i in range(1, n):
    for j in range(i):
        print(" ", end='')
    c = chr(65+i)
    for j in range(n-i):
        print(c, end=' ')
        c = chr(ord(c)+1)
    print()
