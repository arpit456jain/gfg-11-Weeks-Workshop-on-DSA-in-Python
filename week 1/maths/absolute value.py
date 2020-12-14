#{
#Driver Code Starts
# Initial Template for Python 3



 # } Driver Code Ends

# User function Template for python3

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