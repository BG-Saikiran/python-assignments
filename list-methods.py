#ADDING METHODS
list1 = [34,2,16,74,39]
list1.append(52) # Add an element to the end of the list. 
print(list1)  #[34, 2, 16, 74, 39, 52]

list1.extend([2,5,8])  #Adds all elements from another iterable
print(list1) #[34, 2, 16, 74, 39, 52, 2, 5, 8]

list1.insert(2,31)  #Inserts an element 32 at position 2.
print(list1)  #[34, 2, 31, 16, 74, 39, 52, 2, 5, 8]

#REMOVING METHODS

list2 = [34,2,16,34,74,39]
list2.remove(34)  #Removes the first occurrence of element 34.
print(list2)  #[2, 16, 74, 39]

list2.pop()  #Removes and returns the element at index i. If i not given, removes the last element
print(list2)  #[2, 16, 34, 74]

list2.clear()
print(list2)  #[]

#SEARCHING METHODS

list3 = [34,2,16,16,34,2,74,39]
print(list3.index(2,2))  #4

print((list3.count(16)))  #2

#SORTING/REVERSING METHODS

list3 = [34,2,16,16,34,2,74,39]
list3.reverse()
print(list3)  #[39, 74, 2, 34, 16, 16, 2, 34]

list3.sort()
print(list3)  #[2, 2, 16, 16, 34, 34, 39, 74]
