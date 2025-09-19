while True:
    pattern_size = int(input("Enter the size of the pattern: "))
    if pattern_size  > 0:
        break
    else:
        print("Please enter a positive integer")
row = 0
while row < pattern_size:
    row += 1
    for column in range(pattern_size):
        
            print("*", end="")
    print()
    