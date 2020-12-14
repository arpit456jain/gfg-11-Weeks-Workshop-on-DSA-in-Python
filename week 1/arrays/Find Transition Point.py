
def transitionPoint(arr, n):
    #Code here
    for i in range(n):
        if arr[i] == 1:
            return i
    else:
        return -1


#{
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends