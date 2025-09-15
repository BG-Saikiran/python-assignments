#Reverse a string

#Method-1
str1 = "python"
str1 = str1[: : -1]
print(str1)

#Method-2
str1 = "python"
str2 = ""
for ch in range(len(str1)-1, -1, -1):
    str2 += str1[ch]

print(str2)  

#method-3
str1 = "python"
str2 = ""
for ch in str1:
    str2 = ch + str2
print(str2)    

#method-4 -> does not support item assignment because string is a immutable Datatype
# str1 = "python"
# first = 0
# last = len(str1) - 1
# while first < last:
#     str1[first],str1[last] = str1[last], str1[first]
#     first += 1
#     last -= 1

# print(str1)    

#method-5
str1 = "Hello"
print("".join(reversed(str1)))
    

#method-6
from functools import reduce

s = "python"
rev = reduce(lambda first, second: second + first, s)
print(rev)    




# [123, 145, 326, 908] -> [6, 10, 11, 17]
#Method-1
list1 = [123, 145, 326, 908] 
list2 = []
for i in list1:
    sum = 0
    while 0<i:
        rem = i%10
        sum += rem
        i = i//10
    list2.append(sum)
print(list2)    

#Method-2
list1 = [123, 145, 326, 908] 
list2 = []
for i in list1:
    sum = 0 
    for j in str(i):
        sum += int(j)
    list2.append(sum)
print(list2)        



#max value in digits
num = 45937
value = 0
while 0 < num:
    rem = num % 10 
    if rem > value:
        value = rem
    num = num // 10

print(value)        
    

#[123, 456, 789, 51, 33] => [3,6,9,1,3]

list1 = [123, 456, 789, 51, 33]
list2 = []
for i in list1:
    last_digit = ""
    for j in str(i):
        last_digit += j
    v = last_digit[-1:-2:-1]
    list2.append(v)
print(list2)  


list1 = [123, 456, 789, 51, 33]
list2 = []
for i in list1:
    while 0 < i:
        rem = i % 10
        break
    list2.append(rem)
print(list2)     


list3 = [i % 10 for i in list1]
print(list3)


