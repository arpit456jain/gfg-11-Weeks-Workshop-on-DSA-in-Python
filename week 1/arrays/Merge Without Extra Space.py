# User function Template for python3

def merge(arr1, arr2, n, m):
    # code here
    myarr = []
    myarr = arr1 + arr2
    # print(myarr)
    myarr.sort()
    arr1[:] = myarr[0:n]
    arr2[:] = myarr[n:]
    # print(arr1,arr2)


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n, m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        merge(arr1, arr2, n, m)
        print(*arr1, end=" ")
        print(*arr2)
# } Driver Code Ends