#User function Template for python3

def findMissing(arr, size):
    # your code goes here
    for i in range(1,size+1):
        if i in arr:
            # print(i)
            pass
        else:
            return i


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(findMissing(arr, n))
# } Driver Code Ends