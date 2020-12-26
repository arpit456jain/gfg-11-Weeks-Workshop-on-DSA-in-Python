# User function Template for python3

# arr[] : input list of size n
# k     : as specified in the problem description
# Return a list that consists of the Top K most frequent elements in arr
def TopK(arr, n, k):
    has_map = {}
    arr.sort()
    arr = arr[::-1]
    print(arr)
    for i in arr:
        if i in has_map.keys():
            has_map[i] = has_map[i] + 1
        else:
            has_map[i] = 1

    print(has_map)
    return arr


t = int(input())

for tc in range(t):
    inp = list(map(int, input().split()))
    n = inp[0]
    arr = inp[1:]
    k = int(input())

    res = TopK(arr, n, k)

    for i in res:
        print(i, end=" ")

    print()


# } Driver Code Ends