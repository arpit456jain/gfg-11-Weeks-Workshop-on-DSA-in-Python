import math
# function to convert binary string to gray string
def decimalToBinary(n):
    binary = ""
    while(n>0):
        r=n%2
        binary = str(r)+binary
        n=n//2
    return binary
def binaryToDecimal(str1):
    num=0
    j=0
    for i in range(len(str1)-1,-1,-1):
        bitvalue = int(str1[i]) * int(math.pow(2,j))
        j=j+1
        num = num + bitvalue
        # print(bitvalue)
    # print(num)
    return  num

def binarytoGray(binary):
    gray = "";

    # MSB of gray code is same as binary code
    gray += binary[0]
    # Compute remaining bits, next bit is comuted by doing XOR of previous and current in Binary
    for i in range(1, len(binary)):
        prev = int(binary[i - 1])
        cur = int(binary[i])
        # Concatenate XOR of previous bit with current bit
        gray += str(prev^cur)
    return gray;


# function to convert gray code string to binary string
def graytoBinary(gray):
    binary = ""
    # MSB of binary code is same as gray code
    binary += gray[0];
    # Compute remaining bits
    for i in range(1, len(gray)):
        # If current bit is 0,
        # concatenate previous bit
        if (gray[i] == '0'):
            binary += binary[i - 1];

        # Else, concatenate invert
        # of previous bit
        else:
            if binary[i - 1] == '1':
                binary += '0'
            else:
                binary += '1'

    return binary;



# Driver Code
a=int(input())
binary = decimalToBinary(a)
print("binary reprsentation of ",a," is ",binary)
gcode = binarytoGray(binary)
print("Gray code of", binary, "is",gcode)
bcode = graytoBinary(gcode)
print("Binary code of", gcode, "is",bcode)
print(binaryToDecimal(bcode))

