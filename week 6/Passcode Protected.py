#User function Template for python3



# return the smallest number permutation
def findSmallestPermutation(num):
    nstr = str(num)
    lstr = list(nstr)
    lstr.sort()
    nstr = "".join(lstr)
    num = int(nstr)
    # print(nstr,num)
    return num
def passcode_protected(n):
    has_map = {}
    for i in range(1,n+1):
        smallestper= findSmallestPermutation(i)
        # print(smallestper)
        if smallestper in has_map.keys():
            pass
        else:
            has_map[smallestper] = True
    # print(has_map)
    # print(len(has_map))
    return len(has_map)

def countNumber(n):
	result = 0

	# Pushing 1 to 9 because all number
	# from 1 to 9 have this property.
	for i in range(1, 10):
		s = []
		if (i <= n):
			s.append(i)
			result += 1

		# take a number from stack and add
		# a digit smaller than last digit
		# of it.
		while len(s) != 0:
			tp = s[-1]
			s.pop()
			for j in range(tp % 10, 10):
				x = tp * 10 + j
				if (x <= n):
					s.append(x)
					result += 1

	return result
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(countNumber(n))
        # print(passcode_protected(n))
# } Driver Code Ends