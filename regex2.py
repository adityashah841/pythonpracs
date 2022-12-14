import re
lines=["983765356","1234567890","9780934567","826262626666"]
pattern =r"[7|8|9][0-9]{9}"
x=[]
for i in lines:
    y=re.findall(pattern,i)
    if len(y)>0 and y[0]==i:
        x.append(y[0])
print(x)
