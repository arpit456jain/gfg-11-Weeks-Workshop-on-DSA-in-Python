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

    while (i <=n-1 and j <=m-1):

        if a[i] < b[j]:
            i = i + 1   
        elif a[i] == b[j]:
            if len(lst) > 0 and lst[-1] == a[i]:
                pass
            else:
                lst.append(a[i])
            i = i + 1
            j = j + 1
        elif b[j] < a[i]:
            j=j+1

    print(lst,i,j)

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