# User function Template for python3

class stack:
    def __init__(self):
        self.s = []
        self.minEle = None

    def push(self, x):
        self.s.append(x)

    def pop(self):
        try:
            return  self.s.pop()
        except:
            return -1

    def getMin(self):
        try:
            self.minEle = min(self.s)
        except:
            self.minEle = -1
        return self.minEle

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk = stack()

        qi = 0
        qn = 1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi + 1])
                qi += 2
            elif qt == 2:
                # print(stk)
                print(stk.pop(), end=' ')
                qi += 1
            else:
                print(stk.getMin(), end=' ')
                qi += 1
            qn += 1
        print()

# } Driver Code Ends