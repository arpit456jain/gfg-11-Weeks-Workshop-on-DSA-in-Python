# User function Template for python3

def majorityWins(arr, n, x, y):
    # code here
    c1 = 0
    c2 = 0
    for i in arr:
        if i == x:
            c1 = c1 + 1
        if i == y:
            c2 = c2 + 1
    # print(c1,c2)
    if c1 > c2:
        return x
    if c2 > c1:
        return y
    if c1 == c2:
        if x < y:
            return x
        else:
            return y


# {
#  Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        x, y = map(int, input().strip().split())

        print(majorityWins(arr, n, x, y))
        T -= 1

# } Driver Code Ends