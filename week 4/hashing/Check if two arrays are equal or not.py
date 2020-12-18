# User function Template for python3
def check(arr1, arr2, n):
    dic1={}
    for i in arr1:
        try:
            if dic1[i] == 1:
                dic1[i] = dic1[i] + 1
        except:
            pass
        dic1[i] = 1
    # print(dic1)
    for i in arr2:
        try:
            dic1[i] = dic1[i] - 1
        except:
            pass
    # print(dic1)
    for i in dic1.keys():
        if dic1[i]!=0:
            return False
    return True
def check2(arr1, arr2, n):
    # return: True or False
    #method 1 sorting
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False

    # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB


if __name__ == '__main__':
    t = int(input())
    for tc in range(t):

        n = int(input())

        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        if check(arr1, arr2, n):
            print(1)
        else:
            print(0)

# } Driver Code Ends