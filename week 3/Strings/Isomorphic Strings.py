# User function Template for python3
'''
	Your task is to check if the given strings are
	isomorphic or not.

	Function Arguments: str1 and str2 (given strings)
	Return Type: boolean

'''


def areIsomorphic2(str1, str2):
    # it will check one to one mapping from str1 to str2 for every char
    dict1 = {}
    len1 = len(str1)
    len2 = len(str2)
    # print(dict1,len1,len1)
    if len1 == len2:
        for  i in range(len1):
            if str1[i] in dict1.keys():
                    if dict1[str1[i]] == str2[i]:
                        pass
                    else:
                        return False
            else:
                dict1[str1[i]] = str2[i]
    else:
        return False
    return True
def areIsomorphic(s,p):
    first = areIsomorphic2(s, p)
    second = areIsomorphic2(p, s)
    # print(first, second)
    if (first == True and second == True):
        return True
    else:
        return False

if __name__ == '__main__':
    # t = int(input())
    t=1
    for i in range(t):
        # s = str(input())
        # p = str(input())
        s="pijthbsfy"
        p="fvladzpbf"
        if (areIsomorphic(s, p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends