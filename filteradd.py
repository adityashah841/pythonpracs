# x = [1,2,3,4]
# y=[4,2,3,1]

# def add(a,b):
#     return a+b
# z = list(map(add,x,y))
# print(z)
# Code filter and Map:
x = input("Enter list of elements: ")
x=x.split(" ")
x = [int(i) for i in x]
z =list(map(lambda a: a**3 ,filter(lambda a: a if a%2==1 else None, x)))
print(z)
