# User function Template for python3

def firstRepeated(arr, n):
    # arr : given array
    # n : size of the array
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return i + 1
    else:
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(firstRepeated(arr, n))
# } Driver Code Ends    