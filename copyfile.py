f1=open("copyfile1.txt","r")
lines=f1.readlines()
new_lines=[]
for i in lines:
    new_lines.append(i.replace("\n",""))
print(new_lines)
f1.close()

f2 = open("copyfile2.txt","w")
f2.writelines(new_lines)
f2.close()
