word = input("Enter a line: ")
frequency = {}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print("Count of all characters: ", frequency)