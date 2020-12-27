# {
# Driver Code Starts

# } Driver Code Ends

def reverse(s):
    stack1 = []
    for i in s:
        stack1.append(i)
    s=""
    while(len(stack1)>0):
        s = s + stack1.pop()
    return s
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        print(reverse(str1))
# } Driver Code Ends