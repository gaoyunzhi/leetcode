class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        ans = 1.0
        if m < n:
            m, n = n, m
        for i in xrange(n - 1):
            ans *= (n + m - 2 - i) * 1.0 / (i + 1) 
        return int(ans + 0.9)

sol = Solution()
print sol.uniquePaths(3, 3)