# User function template for Python

class Solution:
    def reverseInGroups(self, arr, N, K):
        arr1 = []
        if K >= N:
            arr1 = arr
            arr1.reverse()
            arr[:] = arr1

        else:
            arr1 = []
            for i in range(0, N, K):
                # print(i)
                lst = arr[i:i + K]
                lst.reverse()
                # print(lst)
                for i in lst:
                    arr1.append(i)
            # print(arr1)
            arr[:] = arr1


# {
#  Driver Code Starts
# Initial template for Python

import math


def main():
    T = int(input())
    while (T > 0):
        nk = [int(x) for x in input().strip().split()]
        N = nk[0]
        K = nk[1]
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        ob.reverseInGroups(arr, N, K)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends