class Solution:
    def getIsMatch(self, n, m):
        if m <= -1 and n >= 0:
            return False
        if self.p[m] == '*':
            if self.getIsMatchRem(n, m - 2):
                return True
            for i in xrange(n, -1, -1):
                if not self.alphaMatch(self.s[i], self.p[m - 1]):
                    return False
                if self.getIsMatchRem(i - 1, m - 2):
                    return True
        if n <= -1 or not self.alphaMatch(self.s[n], self.p[m]):
            return False
        return self.getIsMatchRem(n - 1, m - 1)

    def alphaMatch(self, alpha, matchAlpha):
        return matchAlpha == '.' or alpha == matchAlpha

    def getIsMatchRem(self, n, m):
        if not (n, m) in self.isMatchCache:
            self.isMatchCache[(n, m)] = self.getIsMatch(n, m)
        return self.isMatchCache[(n, m)]

    # @return a boolean
    def isMatch(self, s, p):
        self.s = s
        self.p = p
        self.isMatchCache = {(-1, -1): True}
        return self.getIsMatchRem(len(s) - 1, len(p) - 1)

sol = Solution()
print sol.isMatch("aa","a")
print sol.isMatch("aa","aa") 
print sol.isMatch("aaa","aa") 
print sol.isMatch("aa", "a*") 
print sol.isMatch("aa", ".*")
print sol.isMatch("ab", ".*")
print sol.isMatch("aab", "c*a*b")
print sol.isMatch("", "c*")
print sol.isMatch("aaa", "aaaa")
