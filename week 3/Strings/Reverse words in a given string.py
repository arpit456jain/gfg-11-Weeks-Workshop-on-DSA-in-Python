# User function Template for python3

#reverse the string without reversing its individual words. Words are separated by dots.
# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
def reverseWords(S):
    lst=[]
    a=0
    b=0
    for i in range(len(S)):
        if S[i] == '.':
            b=i
            word = S[a:b]
            a=i+1
            lst.append(word)
            # print(word)
    #last word
    lst.append(S[a:])
    # print(lst)
    finalstr=""
    for i in range(len(lst)-1,-1,-1):
        finalstr = finalstr +lst[i] + "."
    # print(finalstr)
    finalstr = finalstr[0:len(finalstr)-1]
    # print(finalstr)
    return finalstr
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))

# } Driver Code Ends