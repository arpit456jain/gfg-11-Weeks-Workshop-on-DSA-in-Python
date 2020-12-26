def firstRepeating(arr, n):
    dict1 = {}
    min_index=-1
    for i in range(n-1,-1,-1):
        if arr[i] in dict1.keys():
            min_index = i
        else:
            dict1[arr[i]] = i
    if min_index == -1:
        return -1
    return min_index+1
def printNonRepeated(arr, n):
    dict1 = {}
    arr2 = []
    for i in arr:
        if i in dict1.keys():
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    # print(dict1)
    for i,j in dict1.items():
        if dict1[i] == 1:
            arr2.append(i)
    # print(arr2)
    return arr2

def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        l1 = printNonRepeated(arr, n)
        l2 = firstRepeating(arr,n)
        # print(*l1)
        print(l2)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends