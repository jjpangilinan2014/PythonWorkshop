#Task2
#Simulation: input number: 4
#Simulation: 4-1: 3;



number = input("Number: ")
storeNum = 1
for i in range(1,int(number)+1):
    storeNum *= i

print("The factorial of "+ str(number) +" is " +str(storeNum))
