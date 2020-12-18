def getallcombination(test_str):

    res = [test_str[i: j] for i in range(len(test_str))
               for j in range(i + 1, len(test_str) + 1)]
    print(res)
    return res
test_str = input()
getallcombination(test_str)