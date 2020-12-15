
def isAnagram(a, b):
    a1=list(a)
    b1= list(b)
    a1.sort()
    b1.sort()
    print(a1,b1)
    if a1 == b1:
        return True
    print(a,b)
    return  False





if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # "enter two string with space btw them"
        a, b = map(str, input().strip().split())
        if (isAnagram(a, b)):
            print("YES")
        else:
            print("NO")
            # } Driver Code Ends