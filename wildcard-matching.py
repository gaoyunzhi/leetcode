class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        m = len(p)
        sol = [[True]]
        for (order, pattern_alphabet) in enumerate(p):
            if pattern_alphabet == '*':
                sol[0].append(sol[0][order])
            else:
                sol[0].append(False)
        for (ind, alphabet) in enumerate(s):
            sol.append([])
            sol[ind + 1].append(False)
            for (order, pattern_alphabet) in enumerate(p):
                if pattern_alphabet == '*':
                    sol[ind + 1].append(
                        sol[ind + 1][order] or sol[ind][order + 1]
                    )
                    continue
                if pattern_alphabet == '?':
                    sol[ind + 1].append(sol[ind][order])
                    continue
                if pattern_alphabet != alphabet:
                    sol[ind + 1].append(False)
                    continue
                sol[ind + 1].append(sol[ind][order])
        return sol[-1][-1]
                   
sol = Solution()
print sol.isMatch("aa","a")
print sol.isMatch("aa","aa") 
print sol.isMatch("aaa","aa") 
print sol.isMatch("aa", "*") 
print sol.isMatch("aa", "a*")
print sol.isMatch("ab", "?*")
print sol.isMatch("aab", "c*a*b") 


