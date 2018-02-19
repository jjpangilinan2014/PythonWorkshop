
wii = 0
count = 0
x = 0
mayPera = False
def available():
    global count, x
    if(int(x) >= int(wii)):
        while( int(x) >= int(wii)):
            count = count + 1
            x = int(x)
            x = int(x) - int(wii)
    else:
        print("Ipon muna bes")
        
wii = input("Magkano ba Wii? ")

x = input("Input your ipon: " )

available()

print("Remaining money: " + str(x) + ". Ilang Wii's " + str(count) )
