num = int(input("Enter Number of rows you want to print Pattern : "))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*", end=" ")
    print()