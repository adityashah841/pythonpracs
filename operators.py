#Demonstrate the following Operators in Python with suitable examples. 
# i) Arithmetic Operators 
a = 10
b = 5
print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a % b) #modulus
print(a ** b) #exponent
print(a // b) #floor division

# ii) Relational Operators
print(a == b) #equal to
print(a != b) #not equal to
print(a > b) #greater than
print(a < b) #less than
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to

# iii) Assignment Operator 
a = 10
b = 5
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a //= b
print(a)
a **= b
print(a)

# iv) Logical Operators 
a = True
b = False
print(a and b) #and
print(a or b) #or
print(not a) #not

# v) Bit wise Operators 

x=10 #00001010
y=7  #00000111

print(x&y)  #00000010
print(x|y)  #00001111
print(x^y)  #00001101
print(~x)   #11110101
print(x>>2) #00000010
print(x<<2) #00000010
# vi) Ternary Operator 
a = 10
b = 5
print(a if a > b else b)

# vii) Membership Operators 
a = [1, 2, 3, 4, 5]
print(1 in a)
print(6 not in a)

# viii) Identity Operators
a = 10
b = 10
print(a is b)
print(a is not b)

#comparison

print(2==3)
print(2!=3)
print(2>3)
print(2<3)
print(2>=3)
print(2<=3)


#logical

print(2>3 and 3>4)
print(2>3 or 3>4)
print(not 2>3)


