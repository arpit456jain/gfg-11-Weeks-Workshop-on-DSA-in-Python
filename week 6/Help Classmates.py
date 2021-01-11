# User function Template for python3

def help_classmate(arr, n):
    #actually we have to find next smallest number
    lst=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                lst.append(arr[j])
                break
        else:
            lst.append(-1)
    # print(lst)
    return lst

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        result = help_classmate(arr, n)
        for i in result:
            print(i, end=' ')
        print()

# } Driver Code Ends