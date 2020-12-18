#User function Template for python3


def checpalindrome(str):
    if str[::] == str[::-1]:
        return True
    else:
        return False
# you need to complete this function
def longestPalindrome(test_str):
    res = [test_str[i: j] for i in range(len(test_str))
           for j in range(i + 1, len(test_str) + 1)]
    # print(res)
    max1=0
    str1 = ""
    for i in res:
        a=checpalindrome(i)
        if a == True:
            if len(i) > max1:
                max1 = len(i)
                str1 = i
    return str1


def longestPalSubstr(st):
    n = len(st)  # get length of input string

    # table[i][j] will be false if substring
    # str[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y
             in range(n)]

    # All substrings of length 1 are
    # palindromes
    maxLength = 1
    i = 0
    while (i < n):
        table[i][i] = True
        i = i + 1

    # check for sub-string of length 2.
    start = 0
    i = 0
    while i < n - 1:
        if (st[i] == st[i + 1]):
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    # Check for lengths greater than 2.
    # k is length of substring
    k = 3
    while k <= n:
        # Fix the starting index
        i = 0
        while i < (n - k + 1):

            # Get the ending index of
            # substring from starting
            # index i and length k
            j = i + k - 1

            # checking for sub-string from
            # ith index to jth index iff
            # st[i + 1] to st[(j-1)] is a
            # palindrome
            if (table[i + 1][j - 1] and
                    st[i] == st[j]):
                table[i][j] = True

                if (k > maxLength):
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1


    return maxLength  # return length of LPS


if __name__=='__main__':
    # tc=int(input())
    tc=1
    for _ in range(tc):
        # str=input()
        str = "abcd"
        print(longestPalindrome(str))
        print(longestPalSubstr(str))
# } Driver Code Ends