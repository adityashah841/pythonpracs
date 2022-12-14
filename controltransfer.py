# Demonstrate the following control transfer statements in Python with suitable examples.
# i) break
# ii) continue
# iii) pass

# i) break
# The break statement is used to terminate the loop or statement in which it is present
for x in range(1, 11):
    if x == 5:
        break
    print(x)

# ii) continue
# The continue statement is used to skip the current iteration of the loop and continue with the next iteration
for x in range(1, 11):
    if x == 5:
        continue
    print(x)

# iii) pass
# It is like null operation, as nothing will happen is it is executed. Pass statement can also be used for writing empty loops
for letter in 'Python': 
   if letter == 'h':
      pass
      print('This is pass block')
   print('Current Letter :', letter)

print("Good bye!")
