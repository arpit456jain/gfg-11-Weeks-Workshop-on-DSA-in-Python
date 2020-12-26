'''
	Your task is to return the index of the pattern
	present in the given string.

	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.

'''

def strstr2(s, p):
    #by rabin kab algo but without hashing
    print("string is",s,"and pattern is",p)
    strlen = len(s)
    pattern_len = len(p)
    i=0
    j=pattern_len - 1
    while(j<strlen):
        sbustring=s[i:j+1]
        print(sbustring)
        if(sbustring == p):
            print("equal")
            return i
        i = i+1
        j = j+1
    return -1

def strstr(s, p):
    print(s,p)
    M = len(p)
    N = len(s)
    # print(M,N)
    for i in range(0,N-M+1):
        # print(i)
        j=0
        while(j<M):

            # print(i,j)
            if (s[i+j]!=p[j]):
                break
            j = j + 1
        # print(i,j)
        if(j==M):
            print("Pattern found at",i)
            return i

    return -1



if __name__ == '__main__':
    # t = int(input())
    t=1
    for cases in range(t):
        s="GeeksForGeeks"
        p="Fr"
        print(strstr2(s, p))

# } Driver Code Ends