# User function Template for python3

def immediateSmaller(arr, n, x):
    # return required ans
    # code here
    arr.sort()
    # print(arr)
    if arr[0] >= x:
        return -1
    for i in range(n):
        if arr[i] >= x:
            # print(arr[i-1])
            return arr[i - 1]


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(e) for e in input().split()]
        x = int(input())

        ans = immediateSmaller(arr, n, x)
        print(ans)
# } Driver Code Ends