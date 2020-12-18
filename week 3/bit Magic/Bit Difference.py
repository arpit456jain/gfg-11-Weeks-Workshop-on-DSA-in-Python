# User function Template for python3

##Complete this function

def countBitsFlip(a, b):
    counter =0
    if a>b:
        a,b = b,a
    while(b>0):
        # print(a%2)
        if (a%2) == (b%2):
            pass
        else:
            counter = counter + 1
        a=a//2
        b=b//2
    return counter
import math
def countflip(a,b):
    num=a^b
    c=0
    while num>0:
        if num%2==1:
            c=c+1
        num=num//2
    return c


def main():
    T = int(input())

    while (T > 0):
        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        print(countBitsFlip(a, b))
        print(countflip(a,b))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends