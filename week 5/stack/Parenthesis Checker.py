#User function Template for python3
'''
Function Arguments :
		@param  : s (given string containing parenthesis)
		@return : boolean True or False
'''
def ispar(x):
    hashmap = {'{':'}','[':']','(':')'}
    print(x,type(x))
    stack1 = []
    for i in x:
        print(i)
        if i == '(' or i == '[' or i == '{':
            stack1.append(i)
        else:
            print("in else")
            if len(stack1) == 0:
                print("stack empty")
                return False
            else:

                if hashmap[stack1[-1]] == i:
                    print("before poping",stack1)
                    stack1.pop()
                    print("after poping",stack1)
                else:
                    print("appending")
                    stack1.append(i)

    print("final stack is",stack1)
    if len(stack1)!=0:
        return False
    return True

if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = "{}{(}))}"
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends