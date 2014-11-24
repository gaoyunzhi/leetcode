class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        forward = [0]
        min_p = prices[0]
        for p in prices[1:]:
            if p < min_p:
                min_p = p
            forward.append(max(p - min_p, forward[-1]))
        max_p = prices[-1]
        backward = [0]
        for p in prices[n - 2:: -1]:
            if max_p < p:
                max_p = p
            backward.append(max(max_p - p, backward[-1]))
        ans = 0
        for i in xrange(n):
            if ans < forward[i] + backward[n - i - 1]:
                ans = forward[i] + backward[n - i - 1]
        return ans


sol = Solution()
print sol.maxProfit([2,9,2,3,8,1,5,8,4,3,6,4,4])
print sol.maxProfit([2,9,2,3,8,1,5,8,4,3,6,4,4]) == 14