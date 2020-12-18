# User function Template for python3


##Complete this function
def swapBits(x):
    # Get all even bits of x
    even_bits = x & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = x & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    return (even_bits | odd_bits)
import math


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        print(swapBits(n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends