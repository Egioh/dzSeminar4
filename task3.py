# # Задайте последовательность чисел. 
# # Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
NumList=[2,3,5,5,3,2,1,6,9,8,7,4,4,12,12]
count =1
tempList=[]
temp=0
i=1
for i in range (len(NumList)):
    count=1
    temp=NumList[i]
    for j in range(i+1,len(NumList)):
        if NumList[j]==temp:
            count+=1
            
    if count==1:
        tempList.append(temp)

print(tempList)
