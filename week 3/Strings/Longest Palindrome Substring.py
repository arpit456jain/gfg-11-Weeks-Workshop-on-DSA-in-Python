#User function Template for python3


def checpalindrome(str1):
    lenofstr = len(str1)
    # print("len of str is",lenofstr)
    start = 0
    end = lenofstr -1
    while(start<=end):
        if str1[start] == str1[end] :
            pass
        else:
            return False
        start +=1
        end -=1
    return True

# you need to complete this function
def longestPalindrome2(test_str):
    # T.c is very high more than O(n^2)
    if checpalindrome(test_str):
        return test_str
    else:

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

#function to print the matrix
def printMatrix(arr):
    for i in arr:
        print(*i)
    return

def longestPalindrome(test_str):
    # T.C = O(n^2)
    if test_str == test_str[::-1]:
        # print("original string itself palindrome")
        return test_str
    str_len = len(test_str)
    if str_len == 1:
        return test_str
    elif str_len == 2:
        if test_str[0] == test_str[1]:
            return test_str
        else:
            return test_str[0]
    elif str_len >= 3:

        matrix = [[0 for x in range(str_len)] for y in range(str_len)]
        # first make all diognal elements 1 because 1 letter is
        # always a palindrome
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    matrix[i][j] = 1
        # printMatrix(matrix)

        # now we make 2 letter string as palindrome if equal
        str = test_str[0]
        maxlen = 1
        start = 0
        end = 1
        while (end < len(test_str)):
            # print(start, end)
            if test_str[start] == test_str[end]:
                matrix[start][end] = 1
                if end - start + 1 > maxlen:
                    maxlen = end - start + 1
                    str = test_str[start:end + 1]
            start += 1
            end += 1

        # printMatrix(matrix)

        #now for string greater than equal to 3 we will iterate string
        #insert 1 if palindrome
        #for to be palindrome 1. s[start] == s[end]
                            # 2. non boundray substring should be palindrome
        # we need two loops for updating whole matrix
        i=2
        start = 0
        end = 2
        while(end-start)!=str_len-1:
            start = 0
            end = start + i
            # print("inside loop", start, end)
            while(end<str_len):
                # print(start,end)
                if test_str[start] == test_str[end] and matrix[start+1][end-1] ==1:
                    matrix[start][end] = 1
                    # print(start, end,maxlen)
                    if end - start + 1> maxlen:
                        maxlen=end-start+1
                        str = test_str[start:end+1]
                start +=1
                end+=1
            i=i+1

        # printMatrix(matrix)
        return str

if __name__=='__main__':
    # tc=int(input())
    tc=1
    for _ in range(tc):
        # str=input()
        str = "dabcba"
        print(longestPalindrome(str))