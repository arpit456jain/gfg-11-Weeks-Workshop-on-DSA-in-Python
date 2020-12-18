def isSparse2(n):
    #this is more efficient because we do not use any loop
    if n & (n>>1) == 0:
        return True
    else:
        return False
def isSparse(n):
    c=0
    while(n>0):
        if (n%2 == 0):
            c=0
        elif (n%2==1):
            c=c+1
        if c>=2:
            return False
        n=n//2
    return True

def main():
    T = int(input())

    while (T > 0):

        n = int(input())
        print(isSparse(n))
        print(isSparse2(n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends