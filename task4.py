import random
k=int(input("введите степень:"))
list=[]
if k!=0:
    for i in range (k,0,-1):
        rand=random.randint(0,101)
        list.append(rand)
        list.append(f'x**{i}')
        list.append("+")
list.pop(len(list)-1)
list.append("= 0")
print(list)
temp=0
data= open("mnogochlen.txt",'w')
data.writelines("")
data= open("mnogochlen.txt",'a')
for i in range(len(list)):
    list[i]=str(list[i])
    temp=list[i]
    print(temp)
    data.writelines(temp)
data.close
