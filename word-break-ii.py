class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        s = s[ :: -1]
        dict = map(lambda word: word[:: -1], dict)
        answers = [[[]]]
        for i in xrange(len(s)):
            answer = []
            for word in dict:
                if s[i - len(word) + 1 : i + 1] == word:
                    for previous_ans in answers[i - len(word) + 1]:
                        answer.append(previous_ans + [word])
            answers.append(answer)
        answer = map( 
           lambda word_list: map(lambda word: word[:: -1], word_list[:: -1]), 
           answer, 
        )
        return map(lambda word_list: ' '.join(word_list), answer)

        

s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
print sol.wordBreak(s, dict)
