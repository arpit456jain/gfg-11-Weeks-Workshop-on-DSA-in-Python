# User function Template for python3
'''
1
30
9 -10 -1 5 17 -18 6 19 -12 5 18 14 4 -19 11 8 -19 18 -20 14 8 -14 12 -12 16 -11 0 3 -19 16
'''
def findSubArrays(arr, n):
    # T.C = very high more than O(n^2)
    count =0
    for i in range(n):
        j=i
        while(j<n):
            #sllicing the sub arrays
            arr2 = arr[i:j+1]
            print(arr2,sum(arr2))
            if sum(arr2) == 0:
                count = count + 1
            j=j+1

    return count


if __name__ == '__main__':
    # t = int(input())
    t=1
    for tc in range(t):
        # N = int(input())
        N = 6
        # A = [int(x) for x in input().strip().split(' ')]
        A = [0, 0 ,5 ,5 ,0 ,0]
        print(findSubArrays(A, N))

# } Driver Code Ends