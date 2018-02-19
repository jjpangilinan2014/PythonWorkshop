number = input("Number: ")
storeNum = 1
for i in range(1,int(number)+1):
    storeNum *= i

print("The factorial of "+ str(number) +" is " +str(storeNum))
