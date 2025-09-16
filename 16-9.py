#Desending order
list1 = [99,32,67,22,45,87]
for j in range(len(list1)-1, 0, -1): #6
    for i in range(0, j): #6
        if list1[i] < list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
print(list1)  

#String Sorting by length
list1 = ["HEllo", "sai", "kiran"]
for j in range(0,len(list1)-1,): #6
    for i in range(0, j): #0 1 2 3 4 5 6
        if len(list1[i]) > len(list1[i+1]):
            list1[i], list1[i+1] = list1[i+1], list1[i]
print(list1) 

#Can you sort nested lists based on the first element of each nested list.
list1 = [[3,4], [1,2], [9,1], [2,3]]
for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-1-i):
        if list1[j][0] > list1[j + 1][0]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)            
