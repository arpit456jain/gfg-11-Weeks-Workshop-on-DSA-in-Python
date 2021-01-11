#q for recursion
'''
Given a keypad as shown in the diagram, and an n digit number,
 list all words which are possible by pressing these numbers.
'''
hash_map = {0:"",1:"",2:"abc",3:"def",4:"ghi",
                5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

def findCombinations(n,ans):
        if n==0:
            print(ans)
            return
        else:
            for i in range(0,len(hash_map[n%10])):

                findCombinations(n//10,ans+hash_map[n%10][i])



n=int(input())
ans = ""
findCombinations(n,ans)