while True:
    pattern_size = int(input("Enter the size of the pattern: "))
    if pattern_size  > 0:
        break
    else:
        print("Please enter a positive integer")

for i in range(pattern_size):
    for j in range(pattern_size ):
        print("*", end="")
    print()