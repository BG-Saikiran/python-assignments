n = 123456
while n > 0:
    rem = n%10
    if rem%2==0:
        print("Even",rem)
    n = n//10   

def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True    
num1 = 67491
while num1 > 0:
    rem = num1%10
    if prime(rem):
        print(rem,"Prime")
    num1 = num1//10  



    

