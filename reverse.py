fileRead = open("reverse1.txt", "r")
List = list()

f = fileRead.read()
f = f.split(" ")

for line in f:
    List.append(str(line[::-1]))
       

fileWrite = open("reverse2.txt", "w")

for i in range(len(List)):
    fileWrite.write(str(List[i]))
    fileWrite.write("\n")
