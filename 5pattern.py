def pattern(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(i+1))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'*'*(j))

x = int(input("Enter the number of rows you want: "))
pattern(x)
print("Number of lines generated:", x * 2 - 1)