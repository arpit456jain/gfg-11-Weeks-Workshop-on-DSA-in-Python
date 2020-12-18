# User function Template for python3

NO_OF_CHARS = 256
def longestUniqueSubsttr(string):
    # Initialize the last index array as -1, -1 is used to store
    # last index of every character
    lastIndex = [-1] * NO_OF_CHARS

    n = len(string)
    res = 0  # Result
    i = 0

    for j in range(0, n):
        # Find the last index of str[j]
        # Update i (starting index of current window)
        # as maximum of current value of i and last
        # index plus 1
        i = max(i, lastIndex[ord(string[j])] + 1);

        # Update result if we get a larger window
        res = max(res, j - i + 1)

        # Update last index of j.
        lastIndex[ord(string[j])] = j;

    return res
def findchar(str1,ch):
    for i in str1:
        if i == ch:
            return True
    return False
def SubsequenceLength(s):
    # Codee here
    max = 0
    sub = ""
    i=0
    j=1
    while(j<=len(s)):
        sub=s[i:j]
        # print(sub,sub[0:-1])
        if findchar(sub[0:-1],sub[-1]):
            # print("repeat ho gya")
            i=i+1
            j=j-1
        else:
            # print("repeat nhi kr rha hai last char")
            if len(sub)>max:
                max = len(sub)
                # print(max)
        j=j+1
    return max


s = input()
# s="geeksforgeeks"
print(SubsequenceLength(s))

# } Driver Code Ends