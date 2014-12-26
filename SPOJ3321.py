import sys,math

class Solution(object):
    def __init__(self, raw_items):
        raw_items = map(self.parseItem, raw_items)
        self.items = sorted(raw_items, key=self.getValuePerWeight, reverse=True)
        self.cache = {(0, 0): 0}
        self.n = len(self.items)
        self.restValue = [0]
        for item in self.items[:: -1]:
            self.restValue.append(self.restValue[-1] + item[1])
        self.restValue.reverse()

    def parseItem(self, row):
        return map(int, row.split())

    def getValuePerWeight(self, raw_item):
        return raw_item[1] * 1.0 / raw_item[0]

    def getAns(self, c):
        self.max = 0
        return self.findMax(c, 0, 0)

    def findMax(self, c, m, v):
        if v + self.restValue[m + 1] <= self.max:
            return 0
        if not (c, m) in self.cache:
            self.cache[(c, m)] = self.findMaxInternal(c, m, v)
        return self.cache[(c, m)]

    def findMaxInternal(self, c, m, v):
        if v < self.max:
            self.max = v
        if m == self.n or c == 0:
            return 0
        potential_sol = [0]
        if self.items[m][0] <= c:
            potential_sol.append(
                self.findMax(c - self.items[m][0], m + 1, v + self.items[m][1]) + self.items[m][1]
            )
        if self.restValue[m + 1] > max(potential_sol):
            potential_sol.append(self.findMax(c, m + 1, v))
        return max(potential_sol)

def main():
    handler = open('input.txt', 'r') # sys.stdin   
    s = handler.read().splitlines()
    while '' in s: s.remove('')
    while '\n' in s: s.remove('\n')
    c, _ = map(int, s[0].split())
    sol = Solution(s[1:])
    print sol.getAns(c)

if __name__=='__main__':
    main()
