# User function Template for python3

# T:O(m+n)

def mergeArrays(a, b, n, m):
    '''
    one line code
     # lst = a + b
    # lst = list(set(lst))
    # lst.sort()
    '''

    # code here
    i = 0
    j = 0
    lst = []
    print(a,b,n,m)
    while (i <=n-1 and j <=m-1):
        print(i,j)
        if a[i] < b[j]:
            lst.append(a[i])
            print('added 1st list')
            i = i + 1
        elif a[i] == b[j]:
            lst.append(a[i])
            i = i + 1
            j = j + 1
            print('addedequla')
        elif b[j] < a[i]:
            lst.append(b[j])
            print('added of 2nd list')
    print(lst,i,j)
    if i==n:
        while(j<=m-1):
            lst.append(b[j])
            j=j+1
    if j==m:
        while(i<=n-1):
            lst.append(a[i])
            i=i+1
    print(lst)
    return lst




if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        li = mergeArrays(a, b, n, m)
        for val in li:
            print(val, end=' ')
        print()
# } Driver Code Ends