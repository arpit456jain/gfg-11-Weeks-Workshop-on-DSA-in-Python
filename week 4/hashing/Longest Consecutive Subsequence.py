# your task is to complete this function
# your function should return the length of the longest subsequence
def findLongestConseqSubseqByHashing(arr, n):
    has_map = [0*x for x in range(100)]
    for i in range(n):
        has_map[arr[i]] = True
    # print(has_map)
    count=0
    max_count=0
    for i in has_map:
        if i == True:
            count = count + 1
            # print(count)
        else:
            count=0
        max_count = max(max_count,count)
    # print(max_count)
    return max_count

def findLongestConseqSubseq(arr, n):
    # T.c = O(nlogn) because of sorting
    arr.sort()
    arr = set(arr)
    arr = list(arr)
    # print(arr)
    max_count = 0
    i=0
    count = 0
    while(i<len(arr)-1):
        # print(arr[i],arr[i+1])
        if arr[i+1] - arr[i] == 1:
            count = count+1

        else:
            if count>=max_count:
                max_count = count
            count = 0
        # print("i is",i,"and i+1 is",i+1,"and count=",count,max_count)
        i=i+1

    return max_count+1

#{
#  Driver Code Starts
# Driver function
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        print(findLongestConseqSubseqByHashing(arr, n[0]))

# } Driver Code Ends