

def areRotations(s1, s2):
    l1= list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    # print(l1,l2)
    if l1 == l2:
        return True
    else:
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (areRotations(s1, s2)):
            print(1)
        else:
            print(0)

