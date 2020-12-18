#User function Template for python3
'''
Pangram is a sentence containing every letter in the English alphabet.
Given a string, find all characters that are missing from the string,
i.e., the characters that can make the string a Pangram. We need to print output in alphabetic order.

'''

MAX_CHAR = 26
def missingPanagram(Str):
    # A boolean array to store characters
    # present in string.
    present = [False for i in range(MAX_CHAR)]

    # Traverse string and mark characters
    # present in string.
    for i in range(len(Str)):
        if (Str[i] >= 'a' and Str[i] <= 'z'):
            present[ord(Str[i]) - ord('a')] = True
        elif (Str[i] >= 'A' and Str[i] <= 'Z'):
            present[ord(Str[i]) - ord('A')] = True

    # Store missing characters in alphabetic
    # order.
    res = ""

    for i in range(MAX_CHAR):
        if (present[i] == False):
            res += chr(i + ord('a'))

    return res
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(missingPanagram(s))
        t = t-1

# } Driver Code Ends