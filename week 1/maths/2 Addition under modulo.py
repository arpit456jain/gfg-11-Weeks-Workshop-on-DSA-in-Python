"""
Given two numbers a and b, find the sum of a and b. Since the sum can be very large, find the sum modulo 109+7.

Example 1:

Input:
a = 9223372036854775807
b = 9223372036854775807
Output: 582344006
Explanation:
9223372036854775807 + 9223372036854775807
= 18446744073709551614.
18446744073709551614 mod (109+7)
= 582344006
"""
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

