
def findWinner(s):
    count = 0
    n = len(s);
    st = [];

    # ckecking the top of the stack with
    # the i th character of the string
    # add it to the stack if they are different
    # otherwise increment count
    for i in range(n):
        if (len(st) == 0 or st[-1] != s[i]):
            st.append(s[i]);

        else:
            count += 1;
            st.pop();
            # print(c)
        print(s)
    if count%2==1:
        return "Merry"
    else:
        return "Pippin"


if __name__ == '__main__':
    t = int(input())
    # t=1
    for _ in range(t):
        S = input()
        # S = "abc"
        print(findWinner(S))

        # } Driver Code Ends