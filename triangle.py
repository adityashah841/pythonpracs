# Write Python programs to print the following Pattern
'''
        A
       A B
      A B C
     A B C D
    A B C D E
'''
def pattern(n):
    k = 2 * n - 2  # for spaces
    for i in range(0, n):  # for upper triangle
        for j in range(0, k):  # for spaces
            print(" ", end='')  # print space
        k -= 1  # decrement k
        x = 65  # ASCII value of A
        for j in range(0, i + 1):  # for printing alphabets
            print(chr(x), end=" ")  # print alphabet
            x += 1  # increment ASCII value
        print()  # new line

pattern(5)
