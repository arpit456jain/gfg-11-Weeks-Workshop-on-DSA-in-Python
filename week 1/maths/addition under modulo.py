#User function Template for python3

def sumUnderModulo(a,b):
    # code here
    # print(a,b)
    n = 1000000007
    sum = ((a%n)+(b%n))%n
    # print(sum)
    return sum




import atexit
import io
import sys

if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    a=lst[0]
    b=lst[1]
    print(sumUnderModulo(a,b))

