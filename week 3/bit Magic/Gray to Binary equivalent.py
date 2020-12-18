
import math
def greyConverter(n):
    return n ^ (n >> 1)
##Complete this function

def inversegrayCode(n):
    inv = 0;

    # Taking xor until
    # n becomes zero
    while (n):
        inv = inv ^ n;
        n = n >> 1;
    return inv;


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        ans1=inversegrayCode(n)
        print("gray to binary eq of ",n,ans1)
        ans2=greyConverter(ans1)
        print("binary to gray eq of ",ans1,ans2)
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends