""""
Given two integers ‘a’ and ‘m’. The task is to find the smallest modular multiplicative inverse of ‘a’ under modulo ‘m’.



Example 1:

Input:
a = 3
m = 11
Output: 4
Explanation: Since (4*3) mod 11 = 1, 4
is modulo inverse of 3. One might think,
15 also as a valid output as "(15*3)
mod 11"  is also 1, but 15 is not in
ring {0, 1, 2, ... 10}, so not valid.
"""



class Solution:
    ##Complete this function
    def modInverse(self, a, m):
        for i in range(1, m):
            if (i * a) % m == 1:
                return i
        else:
            return -1



def main():
    T = int(input())

    while (T > 0):
        am = [int(x) for x in input().strip().split()]
        a = am[0]
        m = am[1]
        ob = Solution()
        print(ob.modInverse(a, m))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends