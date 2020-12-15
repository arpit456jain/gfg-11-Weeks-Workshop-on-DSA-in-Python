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
if __name__=='__main__':
    # t = int(input())
    t=1
    for i in range(t):
        a = "3333311111111111"
        b = "44422222221111"
        res = CalSum(a,b)
