

def getMaxOccurringChar(s):
    max1 = 0
    maxchar = s[0]
    for i in range(len(s)):
        c=0
        for j in range(len(s)):
            if s[i] == s[j]:
                c=c+1

        if ((c>=max1) and (maxchar >= s[i])):
            max1=c
            maxchar = s[i]
        print(s[i], "occurs", c, "times", "and max char is", maxchar, "and its count is", max1)
    # print(max1,maxchar)
    return maxchar




if __name__ == '__main__':
    # t = int(input())
    t=1
    for i in range(t):
        # s = str(input())
        s="fdsalkjhfh"
        print(getMaxOccurringChar(s))
# } Driver Code Ends