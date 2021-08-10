""""
You are given an interger I, find the absolute value of the interger I.
Example 1:

Input:
I = -32
Output: 32
Explanation:
The absolute value of -32 is 32.
"""
def absolute(I):
    # code here
    if I>0:
        return I
    else:
        return -1*I


#{
#Driver Code Starts.
def main():
    T = int(input()) #Input the number of testcases
    while(T > 0):
        I = int(input()) #input number
        print(absolute(I)) #Call function and print
        T -= 1 #Reduce number of testcases


if __name__ == "__main__":
    main()

#} Driver Code Ends