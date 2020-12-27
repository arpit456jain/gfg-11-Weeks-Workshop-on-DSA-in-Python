class twoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = [None for x in range(n)]
        self.top1 = -1
        self.top2 = n

    def printstack(self):
        for i in self.arr:
            print(i,end=' ')
        print()
    def push1(self,x):
        if self.top1<self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else:
            print("stak overflow")

    def push2(self,x):
        if (self.top1<self.top2 -1):
            self.top2 = self.top2-1
            self.arr[self.top2] = x
        else:
            print("stack overflow")
    def pop1(self):
        if self.top1>=0:
            popitem = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 = self.top1 - 1
            return popitem
        else:
            return "stack underflow for stack 1 "

    def pop2(self):
        if self.top2 < self.size:
            popitem = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 = self.top2 + 1
            return popitem
        else:
            return "stack underflow for stack 2 "


if __name__ == '__main__':
    t1 = twoStacks(5)
    print('''
    0 for exit
    1 1 item --> push item in stack 1
    1 2 item --> push item in stack 2
    2   1  --> printing stack 1
    2   2  --> printing stack 2
    3   1  --> pop stack 1
    3   2  --> pop stack 2
    ''')
    while(True):
        print("enter the input")
        inputlst = [int(x) for x in input().split()]
        if inputlst[0] == 0:
            break
        if inputlst[0] == 1:
            if inputlst[1] == 1:
                t1.push1(inputlst[2])
            elif inputlst[1] == 2:
                t1.push2(inputlst[2])
            else:
                print("wrong input")
        elif inputlst[0] == 2:
            #printing stacks
            if inputlst[1] == 1:
                t1.printstack()
            elif inputlst[1] == 2:
                t1.printstack()
            else:
                print("wrong choice")
        elif inputlst[0] == 3:
            if inputlst[1] == 1:
                print("poped item from stack 1 is",t1.pop1())
            else:
                print("poped item from stack 2 is",t1.pop2())
        else:
            print("wrong input")
