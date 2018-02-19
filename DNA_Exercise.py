countC = 0
countG = 0
DNA = open("DNA.txt").read();
totalLength = len(DNA)


for i in range(len(DNA)):
    if DNA[i] == "C":
        countC = countC + 1

    if DNA[i] == "G":
        countG = countG + 1

print("Total number of C+G: ", countC+countG)
print("Total Length of DNA: ", len(DNA))
print("Percentage: ", ((countC+countG)/totalLength)*100)
