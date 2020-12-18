# Python3 implementation of the
# above approach

# Function to print the output
def printTheArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")

    print()


# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
    if i == n:
        printTheArray(arr, n)
        return

    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)

    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


# Driver Code
if __name__ == "__main__":
    n = 4
    arr = [None] * n

    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
