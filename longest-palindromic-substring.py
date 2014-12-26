class Solution:
    # @return a string
    def longestPalindrome(self, s):
        n = len(s)
        ans = ''
        maxLen = 0
        inits = [(x, x) for x in xrange(n)] + [(x, x + 1) for x in xrange(n - 1)]
        for left, right in inits:
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > maxLen:
                maxLen = right - left - 1
                ans = s[left + 1: right]
        return ans
        
def test():
    sol = Solution()
    testCases = [
        ['aaa', 'aaa'],
        ['abacc', 'aba'],
        ['ccaba', 'aba'],
        ['abacccc', 'cccc'],
    ]
    for inp, out in testCases:
        if sol.longestPalindrome(inp) != out:
            print inp, out, sol.longestPalindrome(inp)

if __name__ == '__main__':
    test()