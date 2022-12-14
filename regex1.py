import re

lines = ["b6cwwyYt","B3he","a3$","s3iki","e9Bhqia#8"]
pattern = r"[a-k][0|3|6|9][a-z|A-Z|0-9|#]*"
x=[]
for i in lines:
    y=re.findall(pattern,i) 
    if len(y)>0 and y[0]== i:
        x.append(y[0])
print(x)
