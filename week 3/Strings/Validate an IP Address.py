# User function Template for python3

def isValid(S):
    # print(S)
    lst = []
    a = 0
    b = 0
    c = 0
    for i in range(len(S)):
        if S[i] == '.':
            c = c + 1
            b = i
            word = S[a:b]
            a = i + 1
            lst.append(word)
            # print(word)
    # last word
    sum1 = 0
    lst.append(S[a:])
    # print(lst,c)
    if c != 3:
        return 0
    for i in lst:
        if i == "":
            return 0
        if len(i)>=2:
            if i[0] == '0':
                return 0
        if len(i) > 3:
            return 0

        try:
            i1 = int(i)
            # print(i)
            if i1 == 0:
                if len(i) == 1:
                    pass
                else:
                    return 0
            sum1 = sum1 + i1
        except:
            return 0
        if i1 > 255 or i1 < 0:
            return 0
        if sum1 < 0:
            return 0
    return 1
if __name__ == "__main__":
    # t = int(input())
    t=1
    for _ in range(0, t):
        # s = input()
        s = "00.00.00.00"
        # s="172.16.254.01"
        if (isValid(s)):
            print(1)
        else:
            print(0)

# } Driver Code Ends