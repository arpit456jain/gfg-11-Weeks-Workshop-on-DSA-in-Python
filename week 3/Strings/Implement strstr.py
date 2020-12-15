'''
	Your task is to return the index of the pattern
	present in the given string.

	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.

'''


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
        print(strstr(s, p))

# } Driver Code Ends