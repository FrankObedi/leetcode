class Solution:
    def isSubsequence(self, s, t):
        s_iter = 0
        t_iter = 0

        while s_iter < len(s)  and t_iter < len(t):
            if s[s_iter] == t[t_iter]:
                s_iter += 1
                t_iter += 1
            else:
                t_iter += 1
        return s_iter == len(s)
    
s = Solution()
print(s.isSubsequence("axc","ahbgdc"))
print(s.isSubsequence("fan","frank"))