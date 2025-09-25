#A
n = 5
for i in range(n):
    for j in range(n):
        if i == (n) //2 or j == 0 or j == n-1 or i == 0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
print()

#B
n = 5
for i in range(n):
    for j in range(n):
        if i == (n) //2 or j == 0 or j == n-1 or i == 0 or i == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
print()

#C
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()        
print()
n = 5

#E
n= 5 
for i in range(n):
    for j in range(n):
        if j ==0 or i ==0 or i == n-1 or i == (n)//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()    


#F
n= 5 
for i in range(n):
    for j in range(n):
        if j ==0 or i ==0 or i == (n)//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()   


#G
n= 5 
for i in range(n):
    for j in range(n):
        if j ==0 or i ==0 or i == n-1 or ( j == n-1 and i >= n//2) or (i == n//2 and j>= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()   


#H
n= 5 
for i in range(n):
    for j in range(n):
        if j ==0  or j == n-1 or i == (n)//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()   
       

#I
n= 5 
for i in range(n):
    for j in range(n):
        if i ==0  or i == n-1 or j == (n)//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()  

#J
n= 5 
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2 or (i == n-1 and j <= n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 



#L
n= 5
for i in range(n):
    for j in range(n):
        if j ==0  or i == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

#M
n= 5
for i in range(n):
    for j in range(n):
        if j ==0  or j == n-1 or (i == j and i <= n//2) or (i+j == n-1 and i <= n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

#N
n= 5
for i in range(n):
    for j in range(n):
        if j ==0  or j == n-1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

#p
n= 5 
for i in range(n):
    for j in range(n):
        if j == 0 or (j == n-1 and i <= n//2 ) or i == 0 or i == n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

#R
n= 5 
for i in range(n):
    for j in range(n):
        if j == 0 or (j == n-1 and i <= n//2 ) or i == 0 or i == n//2 or (i == j and i >= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

#S
n= 5 
for i in range(n):
    for j in range(n):
        if (j == 0 and i <= n//2) or i == 0 or i == n-1 or i == n//2 or( j == 0 and i <= n//2) or (j == n-1 and i >= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 


#T
n= 5 
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

