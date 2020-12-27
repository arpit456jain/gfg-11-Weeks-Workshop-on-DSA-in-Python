# User function Template for python3

'''
Function Arguments :
		@param  : exp (given postfix expression)
		@return : return the desired value
'''


def EvaluatePostfix(exp):
    # print(exp)
    stack1=[]
    operators = ['+', '-', '*', '/', '(', ')', '^']
    for i in exp:
        if i in operators:
            a = int(stack1.pop())
            b = int(stack1.pop())
            if i == '*':
                c = a * b
            elif i == '+':
                c = a + b
            elif i == '-':
                c = b - a
            elif i == '/':
                c = b//a
            else:
                print("any other optrt",i)
            stack1.append(c)
        else:
            stack1.append(i)
    # print(stack1)
    return stack1.pop()

if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases):
        exp = "231*+9-"
        print('{0:g}'.format(float(EvaluatePostfix(exp))))
# } Driver Code Ends