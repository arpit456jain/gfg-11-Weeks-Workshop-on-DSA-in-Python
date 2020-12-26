# User function Template for python3
def sumofdigits(n):
    sum1 = 0
    while (n):
        r = n % 10
        sum1 = sum1 + r
        n = n // 10
    return sum1


def RulingPair(arr, n):
    # code here
    hash_map = {}
    max1 = -1
    for i in arr:
        sod1 = sumofdigits(i)
        if sod1 in hash_map.keys():
            sum_val = i + hash_map[sod1]
            if sum_val > max1:
                max1 = sum_val
            hash_map[sod1] = max(hash_map[sod1], i)


        else:
            hash_map[sod1] = i
    return max1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(RulingPair(arr, n))

# } Driver Code Ends