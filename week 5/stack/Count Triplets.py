# User function Template for python3
def findTriplets(a, n, sum):
    # Sort the input array
    a.sort()

    # For handling the cases
    # when no such triplets exits.
    flag = False

    # Iterate over the array from
    # start to n-2.
    c=0
    for i in range(n - 2):
        if (i == 0 or
                a[i] > a[i - 1]):

            # Index of the first
            # element in remaining
            # range.
            start = i + 1

            # Index of the last
            # element
            end = n - 1

            # Setting our new target
            target = sum - a[i]

            while (start < end):

                # Checking if current element
                # is same as previous
                if (start > i + 1 and
                        a[start] == a[start - 1]):
                    start += 1
                    continue

                # Checking if current
                # element is same as
                # previous
                if (end < n - 1 and
                        a[end] == a[end + 1]):
                    end -= 1
                    continue

                # If we found the triplets
                # then print it and set the
                # flag
                if (target == a[start] + a[end]):
                    # print("[", a[i], ",",
                    #       a[start], ",",
                    #       a[end], "]",
                    #       end=" ")
                    c=c+1
                    flag = True
                    start += 1
                    end -= 1

                # If target is greater then
                #  increment the start index
                elif (target >
                      (a[start] + a[end])):
                    start += 1

                # If target is smaller than
                # decrement the end index
                else:
                    end -= 1

    # If no such triplets found
    if (flag == False):
        pass
        # print("No Such Triplets Exits")
    return c
def countTriplets(head, x):
    temp = head
    lst = []
    while(temp!=None):
        lst.append(temp.val)
        temp = temp.nxt
    # print(lst)
    a=findTriplets(lst,len(lst),x)

    return a

class Node:
    def __init__(self, x):
        self.val = x
        self.nxt = None


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        x = int(line[1])
        line = input().strip().split()

        head = Node(int(line[0]))
        tail = head
        for i in range(1, n):
            tail.nxt = Node(int(line[i]))
            tail = tail.nxt

        print(countTriplets(head, x))

# } Driver Code Ends