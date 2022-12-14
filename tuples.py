from filecmp import cmp


t = (2,3,4,5,8,7,9,6,1,2,4)
t1 = (3,4,5,8,9,7,5,4,8,6,0)
print(len(t))
print(t.count(2))
print(t.index(8))
print(tuple(sorted(t)))
print(min(t))
print(max(t))
print(cmp(t,t1))
print(tuple(reversed(t)))