#your task is to complete this function
#Function should return the required answer
#You are not allowed to convert string to integer
def remainderWith7(str):
    #Code here
    r = int(str)%7
    return r



#{
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        print(remainderWith7(str))
