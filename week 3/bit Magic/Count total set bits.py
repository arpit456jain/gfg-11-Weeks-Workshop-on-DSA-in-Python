#User function Template for python3

def CountBitsinnum(n):
    # code here
    # return the count
    c=0
    while(n>0):
        if n%2 == 1:
            # print("1",end="")
            c=c+1
        else:
            pass
        # n=n//2
        n=n>>1
    # print(c)
    return c
def CountBits(n):
    c1=0
    for i in range(1,n+1):

        # print("in ",i,"->>",CountBitsinnum(i))
        c1=c1+CountBitsinnum(i)
    return c1
#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        print(CountBits(int(input())))
# } Driver Code Ends