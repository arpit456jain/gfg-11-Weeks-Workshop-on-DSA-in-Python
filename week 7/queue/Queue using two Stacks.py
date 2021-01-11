# User function Template for python3

def Push(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)
    # code here
    # print(stack1)

def Pop(stack1, stack2):
    '''
    stack1: list
    stack2: list
    '''
    if len(stack1) == 0 and len(stack2) == 0:
        #empty
        return -1
    elif len(stack2)==0:
        # copy all values to stack 1 to stack 2 and then pop
        while(len(stack1)!=0):
            pi = stack1.pop()
            stack2.append(pi)
        return stack2.pop()
    else:
        return stack2.pop()

if __name__ == '__main__':
    # test_cases = int(input())
    test_cases = 1
    for cases in range(test_cases):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))

        i = 0
        stack1 = []
        stack2 = []
        while i < len(qtyp_qry):
            # print(i)
            if qtyp_qry[i] == 1:
                Push(qtyp_qry[i + 1], stack1, stack2)
                # print(i)
                i += 2
            else:
                print(Pop(stack1, stack2), end=' ')
                i += 1

        print()
# } Driver Code Ends