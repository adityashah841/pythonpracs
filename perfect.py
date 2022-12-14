def perfect(num):
    l=[]
    for i in range(1,num//2+1): 
     if num%i==0:
        l.append(i) 
    if sum(l)==num:
        return 1 
    else:
        return 0


print(perfect(27))