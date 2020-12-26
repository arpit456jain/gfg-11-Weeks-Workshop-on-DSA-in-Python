def printNonRepeated(arr, n):
    dict1 = {}
    arr2 = []
    for i in arr:
        if i in dict1.keys():
            pass
        else:
            dict1[i] = 1
            arr2.append(i)

    # print(arr2)
    return len(arr2)

def countDistinct2(arr, N, K):
    i=0
    j=K
    result_lst = []
    while(j<=N):
        arr2 = arr[i:j]
        # print(arr2)
        result=printNonRepeated(arr2,len(arr2))
        # print(result)
        result_lst.append(result)
        j=j+1
        i=i+1
    # print(result_lst)
    return result_lst

def countDistinct3(arr, N, K):
    i=0
    j=K
    result = []
    while(j<=N):
        # print(i,j)
        set1 = set(arr[i:j])
        len1 = len(list(set1))
        result.append(len1)
        i=i+1
        j=j+1
    return result

def countDistinct(arr, N, K):
    # this is very efficient t.c O(n)
    hash_map = {}
    resulted_array=[]
    for i in range(K-1):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] = hash_map[arr[i]] + 1
        else:
            hash_map[arr[i]] = 1
    # print(hash_map)
    i=0
    j=K-1
    while(j<N):
        # adding next element
        if arr[j] in hash_map.keys():
            hash_map[arr[j]] = hash_map[arr[j]] + 1
        else:
            hash_map[arr[j]] = 1
        print(hash_map)
        size1 = len(hash_map)
        # print(size1)
        resulted_array.append(size1)

        j = j + 1
        # deleting first element
        if hash_map[arr[i]] == 1:
            # delete arr[i]
            del hash_map[arr[i]]
        else:
            hash_map[arr[i]] = hash_map[arr[i]] - 1
        i = i + 1


    # size1 = len(hash_map)
    # print(hash_map,size1)
    # resulted_array.append(size1)
    print(resulted_array)
    return resulted_array
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends