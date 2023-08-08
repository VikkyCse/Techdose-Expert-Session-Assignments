#828. Count Unique Characters of All Substrings of a Given String

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        ans = [[-1] for _ in range(26)]
        for i in range(n):
            ind = ord(s[i])-65
            ans[ind].append(i)    
        for i in range(n):
            ind = ord(s[i])-65
            ans[ind].append(n)   
        count = 0 
        for i in range(26):
            for j in range(1,len(ans[i])-1):

                count += ((ans[i][j]-ans[i][j-1])*(ans[i][j+1]-ans[i][j]))
        return count
