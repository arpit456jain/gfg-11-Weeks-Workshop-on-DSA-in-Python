#User function Template for python3

def max_of_subarrays(arr,n,k):
    # Time limit excede hor rha tha pr phr optinise kr diya
    # done
    i=0
    j=k
    maxsumlst = []
    maxval=0
    if j == n:
        maxsumlst.append(max(arr))
    else:
        queue = arr[0:k]
        # print(queue)
        maxval=max(queue)
        maxsumlst.append(maxval)
        for i in range(k,n):
            pi=queue.pop(0)
            queue.append(arr[i])
            if pi == maxval:
                maxval = max(queue)
            elif arr[i]>maxval:
                maxval=arr[i]
            else:
                pass
            # print(maxsumlst)
            maxsumlst.append(maxval)
    # print(maxsumlst)
    return maxsumlst


if __name__ == '__main__':
    # test_cases = int(input())
    test_cases=1
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        res = max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends