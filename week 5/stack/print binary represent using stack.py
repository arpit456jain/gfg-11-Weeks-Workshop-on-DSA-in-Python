# Python3 Program for the binary
# representation of a given number


def bin(n):
    stack = []
    while(n>0):
        remainder = n%2
        stack.append(remainder)
        n = n // 2
    while(len(stack)!=0):
        print(stack.pop(),end="")


if __name__ == "__main__":
    bin(7)
    print()
    bin(4)


