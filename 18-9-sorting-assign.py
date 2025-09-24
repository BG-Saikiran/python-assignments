#Count the number of swaps performed by bubble sort while sorting an array.

list1 = [-1,23,42,-10,39,71,86]
count1 = 0
count2 = 0
for i in range(0, len(list1)):
    for j in range(0, len(list1) - 1 - i):
        if list1[j] > list1[j + 1]:
            # list1[j], list1[j + 1] = list1[j + 1], list1[j]
            temp = list1[j + 1]
            list1[j + 1] = list1[j]
            list1[j] = temp
            count2 += 1
        count1 += 1


print(list1,)     
print(f'total swapped elements in one iteration: {count2}')       
print(f'total swapped elements : {count1}')


#Apply binary search in only first half of the list. (Search only in first half)

list1 = [-10, -1, 23, 39, 42, 71, 86]
half_list = len(list1)//2
half_list = list1[:half_list]
low = 0
high = len(half_list) - 1
target = -1
flag = True
while low <= high:
    mid = (low + high) // 2
    if half_list[mid] == target:
        print("found at",mid)
        flag = False
        break

    elif half_list[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
if flag == True:
    print("not found")   

