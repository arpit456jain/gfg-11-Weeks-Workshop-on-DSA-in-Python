# function to return maximum XOR subset in set[]
def maxSubarrayXOR(set, n):
    maxxor = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                print(set[i],set[j],set[i]^set[j])
                xorval = (set[i]^set[j])^set[k]
                maxxor = max(maxxor,xorval)
    # print(maxxor)
    return maxxor

if __name__ == '__main__':
    # t = int(input())
    t=1
    for i in range(t):
        n = int(input())
        # n=3
        set = list(map(int, input().split()))
        # set = [9,8,5]
        print(maxSubarrayXOR(set, n))
# } Driver Code Ends