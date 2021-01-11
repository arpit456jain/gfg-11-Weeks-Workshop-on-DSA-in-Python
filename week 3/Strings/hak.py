#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

def findSubstring(s, k):
    # Write your code here

    max1 = 0
    str2=""
    vowel = ['a','e','i','o','u']
    print(s)
    c=0
    for i in range(k):
        if s[i] in vowel:
            c=c+1
    if c>max1:
        max1=c
        str2=s[0:k]
    print(c,max1,str2)
    i = 0
    j = k
    while(j<len(s)):
        if s[i] in vowel:
            c=c-1
        i=i+1
        if s[j] in vowel:
            c=c+1
        print(c)
        print(s[i:j+1])
        if c>max1:
            max1 = c
            str2 = s[i:j+1]
        j=j+1
    if str2 == "":
        return "Not Found!"
    return str2

if __name__ == '__main__':

    s = "qwdftr"

    k = 2

    result = findSubstring(s, k)
    print(result)

