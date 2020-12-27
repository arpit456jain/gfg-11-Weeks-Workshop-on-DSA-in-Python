#User function Template for python3
def prec(char):
    #return the preceding  val
    if char == '^':
        return 3
    elif char == '*' or char == '/':
        return 2
    elif char == '+' or char == '-':
        return 1
    else:
        return -1

def InfixtoPostfix(exp):
    stack = ['N']
    # print(exp)
    str1 = ""
    operators = ['+' , '-' , '*' , '/' , '(' , ')','^']
    for i in exp:
        # print("in these loop",stack,str1)
        if i in operators:
            if len(stack) == 0:
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while(stack[-1]!='N' and stack[-1]!= '('):
                    c=stack[-1]
                    stack.pop()
                    str1 = str1 + c
                if stack[-1] == '(':
                    stack.pop()
            else:
                #if an oprtor is acanned
                # print(stack,str1,i)
                while(stack[-1]!='N' and prec(i)<=prec(stack[-1])):
                    c = stack[-1]
                    stack.pop()
                    str1 = str1 + c
                stack.append(i)

        else:
            str1 = str1 + i

    while(stack[-1]!='N'):
        c = stack.pop()
        str1 = str1 + c
        # print(stack,str1)
    return str1

if __name__ == '__main__':
    # test_cases = int(input())
    test_cases = 1
    for cases in range(test_cases) :
        # exp = str(input())
        # exp = "a+b*(c^d-e)^(f+g*h)-i"
        exp = "(A+B^D)/(E–F)+G"
        print(InfixtoPostfix(exp))
# } Driver Code Ends