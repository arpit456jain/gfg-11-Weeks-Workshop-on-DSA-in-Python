
def multiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    if len1 == 0 or len2 == 0:
        return "0"

    # will keep the result number in vector
    # in reverse order
    result = [0] * (len1 + len2)

    # Below two indexes are used to
    # find positions in result.
    i_n1 = 0
    i_n2 = 0

    # Go from right to left in num1
    for i in range(len1 - 1, -1, -1):
        carry = 0
        n1 = ord(num1[i]) - 48

        # To shift position to left after every
        # multiplication of a digit in num2
        i_n2 = 0

        # Go from right to left in num2
        for j in range(len2 - 1, -1, -1):
            # Take current digit of second number
            n2 = ord(num2[j]) - 48

            # Multiply with current digit of first number
            # and add result to previously stored result
            # at current position.
            summ = n1 * n2 + result[i_n1 + i_n2] + carry

            # Carry for next iteration
            carry = summ // 10

            # Store result
            result[i_n1 + i_n2] = summ % 10

            i_n2 += 1

        # store carry in next cell
        if (carry > 0):
            result[i_n1 + i_n2] += carry

        # To shift position to left after every
        # multiplication of a digit in num1.
        i_n1 += 1

    # print(result)

    # ignore '0's from the right
    i = len(result) - 1
    while (i >= 0 and result[i] == 0):
        i -= 1

    # If all were '0's - means either both or
    # one of num1 or num2 were '0'
    if (i == -1):
        return "0"

    # generate the result string
    s = ""
    while (i >= 0):
        s += chr(result[i] + 48)
        i -= 1

    return s

def bygeekforgeeks(str1,str2):
    if ((str1[0] == '-' or str2[0] == '-') and
            (str1[0] != '-' or str2[0] != '-')):
        print("-", end='')

    if (str1[0] == '-' and str2[0] != '-'):
        str1 = str1[1:]
    elif (str1[0] != '-' and str2[0] == '-'):
        str2 = str2[1:]
    elif (str1[0] == '-' and str2[0] == '-'):
        str1 = str1[1:]
        str2 = str2[1:]
    ans = (multiply(str1, str2))
    return ans

def CalSum(str1,str2):
    len1=len(str1)
    len2=len(str2)
    res = ""
    c=0
    k=0
    for i in range(min(len1,len2)-1,-1,-1):
        k=k-1
        # print(i)
        a=int(str1[k])
        b=int(str2[k])

        if c==1:
            if len1>len2:
                a=a+1
            else:b=b+1
            c=0
        sum1 = a + b
        if (a+b)>=10:
            c=1
            sum1=sum1%10
        res = str(sum1) + res

    if len1>len2:
        rem = len1-len2
        if c==1:
            carr=int(str1[rem-1])+1
            # print(res,rem,str1[rem-1],carr)
            res = str1[0:rem-1] + str(carr) + res
            c=0
        else:
            res = str1[0:rem] + res
    elif len2>len1:
        rem = len2-len1
        if c==1:
            carr=int(str2[rem-1])+1
            # print(res,rem,str1[rem-1],carr)
            res = str2[0:rem-1] + str(carr) + res
            c=0
        else:
            res = str2[0:rem]  + res
    if c==1:
        res = "1"+res
    # print(res)
    return res
def mylogic(str1,str2):
    print("this is Arpit jain's logic for multiplting two numbers as a string")

    mul1=""
    total = "0"
    len1 = len(str1)
    len2 = len(str2)
    counter = 0
    if len2>len1:
        temp = str1[:]
        str1 = str2[:]
        str2 = temp[:]
        # print(temp,str1,str2)
        len1 = len(str1)
        len2 = len(str2)
    if len1 > len2:
        #y chote wale no me jintnii didgit hai utni baar chalega
        while(len2-1>=0):
            # print("digit of 2nd number is->",len2-1)
            # print("outer")
            i = len1 - 1
            mul1 = "0"*counter
            # print(mul1,counter)
            #y 1st no ko traverse krne k liye
            c=0
            while(i>=0):
                # print(str1[i],str2[len2-1])
                if c!=0:
                    res = int(str1[i]) * int(str2[len2 - 1])
                    # print("there is a carry and i am addind "+c+" to ",res)
                    res = res + int(c)
                    c=0
                else:
                    res = int(str1[i]) * int(str2[len2 - 1])
                if len(str(res))>=2:
                    c=str(res)[0]
                    # print("there is a carry of",c," and i am adding last digit to number",mul1)
                    mul1 = str(res)[-1] + mul1
                else:
                    # print(res)
                    mul1 = str(res) + mul1
                # print(mul1)
                i = i - 1
            #if any carry is left
            if c!=0:
                mul1 = str(c)+mul1
                c=0
            # print("iteration",mul1)
            # total = str(int(total) + int(mul1))
            total  = CalSum(total,mul1)
            len2 = len2 -1
            counter = counter+1
    # print(total)
    return total


 # Driver code
str1 = "1235421415454545454545454544"
str2 = "1714546546546545454544548544544545"
a=bygeekforgeeks(str1,str2)
b=mylogic(str1,str2)

print(a)
print(b)
if a == b:
    print("good job arpit both ans is same")
else:
    print("ans is not same")