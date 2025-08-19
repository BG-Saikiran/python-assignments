def checkArmstrong(num):
    temp = num
    sum = 0
    while temp>0:
        rem = temp%10
        sum += rem**len(str(num))
        temp = temp//10      
    print(num,'=>',sum)
    if sum == num:
        print("arm")
    else:
        print("not arm")

in1 = int(input('enter 1st number: ')) 
in2 = int(input('enter 2nd number: ')) 
for num in range(in1,in2+1):
    checkArmstrong(num)
