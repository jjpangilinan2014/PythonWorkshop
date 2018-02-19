#Task3
#Simulation: insert number: 3
# 
es = ""
def function(x):
    global es
    for i in range(1,int(x)+1):
        es = str(i)
        for j in range(i-1):
            es += str(i)
        print(es)
            

function(input("Insert Number: "))
