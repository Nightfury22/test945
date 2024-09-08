minimum = int(input("Enter the min no: "))
maximum = int(input("Enter the max no: "))
for n in range(minimum, maximum +1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)

num = int(input("Enter a num: "))
print("Prime numbers are: ",end=' ')
for n in range(1, num):
    for i in range(2, n):
        if (n%i)==0:
            break
    else:
        print(n,end= ' ')