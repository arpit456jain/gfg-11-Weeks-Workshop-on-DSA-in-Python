# your task is to complete this function
# function sort the stack such that top element is max
# funciton should return nothing
# s is a stack
def sortedInsert(s, element):
    # Base case: Either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:

        # Remove the top item and recur
        temp = s.pop()
        sortedInsert(s, element)

        # Put back the top item removed earlier
        s.append(temp)


# Method to sort stack


def sorted(s):
    # If stack is not empty
    if len(s) != 0:
        # Remove the top item
        temp = s.pop()

        # Sort remaining stack
        sorted(s)

        # Push the top item back in sorted stack
        sortedInsert(s, temp)
def sorted2(arr):
    print(arr,type(arr))
    lst = []
    #copying all data to an array and sort it
    for i in arr:
        lst.append(i)
    lst.sort()

    #reverse the array and return like a stack
    arr[:]  = lst[::-1]
    print("list",arr)
    return arr

if __name__=='__main__':
    # t = int(input())
    t=1
    for i in range(t):
        # n = int(input())
        n=5
        # arr = list(map(int, input().strip().split()))
        arr = [11 ,2 ,32 ,3 ,41]
        sorted(arr)
        for e in range(len(arr)):
            # print(e,arr)
            print(arr.pop(0), end=" ")
        print()
