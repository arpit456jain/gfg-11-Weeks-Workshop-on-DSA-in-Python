# User function Template for python3
'''
	Your task is to sort the elements according
	to the frequency of their occurence
	in the given array.

	Function Arguments: array a with size n.
	Return Type:Array, the sorted array

'''


def sortByFreq(arr, n):
    hash_map = {}
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]]+=1
        else:
            hash_map[arr[i]]=1
    print(hash_map)
    sorted_array=[]
    sorted_hash_map = sorted(hash_map.items(), key=
    lambda kv: (kv[1], kv[0]))
    print(sorted_hash_map,type(sorted_hash_map))
    for i in range(len(sorted_hash_map)-1,-1,-1):
        # print(sorted_hash_map[i])
        tuple1=sorted_hash_map[i]
        actual_num = tuple1[0]
        no_of_times = tuple1[1]
        while(no_of_times):
            sorted_array.append(actual_num)
            no_of_times=no_of_times-1
    # print(*sorted_array)
    return sorted_array


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        l = sortByFreq(a, n)
        print(*l)
# } Driver Code Ends