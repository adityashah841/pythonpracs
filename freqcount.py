# import collections
# import pprint

# f = open('file1.txt', 'r')
# count = collections.Counter(f.read())
# value = pprint.pformat(count)
# print(value)


import collections
import pprint

f = open('file1.txt', 'r')
count = collections.Counter(f.read())
value = pprint.pformat(count)
print(value)