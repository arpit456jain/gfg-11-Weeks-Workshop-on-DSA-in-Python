
def generate(N):
    queue = []
    for i in range(1,N+1):
        str1=""
        while(i):
            # print(queue)
            r=i%2
            str1=str1+str(r)
            i=i//2
        str1 = str1[::-1]
        queue.append(str1)
    return queue


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends