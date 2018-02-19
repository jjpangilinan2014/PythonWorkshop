#Task3
ez = ""
def function(x):
    global ez
    for i in range(1,int(x)+1):
        ez = str(i)
        for j in range(i-1):
            ez += str(i)
        print(ez)
            

function(input("Insert Number: "))
