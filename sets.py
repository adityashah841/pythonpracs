# NOTE:The discard() method removes the specified item from the set. This method is
# different from the remove() method, because the remove() method will raise an error
# if the specified item does not exist, and the discard() method will not
fruits = {"apple" ,"orange","cherry"}
more = {"guava","mango","cherry"}
fruits.add("banana")
print(fruits)
fruits.update(more)
print(fruits)
cpy = fruits.copy()
print("cpy --" , cpy)
print("clear --" , cpy.clear())
print(fruits.pop())
fruits.discard("grapes")
print(fruits)
fruits.remove("mango")
print(fruits)
print(fruits.union(more))
print(fruits.intersection(more))
print(fruits.difference(more))