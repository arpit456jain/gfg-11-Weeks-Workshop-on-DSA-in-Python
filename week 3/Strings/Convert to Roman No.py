#Your task is to complete this function
#Your function should return a Stringimpo
import math
def convertRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    ans=""
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            # print(sym[i], end="")
            ans = ans + sym[i]
            div -= 1
        i -= 1
    return ans

#{
#  Driver Code Starts
#Your Code goes here
if __name__=='__main__':
    # t = int(input())
    t=1
    for i in range(t):
        # n = int(input())
        n=3549
        print(convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends