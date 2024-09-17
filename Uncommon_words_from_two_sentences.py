class Solution:
    def uncommonFromSentences(self, s1, s2):
        words1 = s1.split()
        words2 = s2.split()
        
        word_count = {}

        for word in words1:
            word_count[word] = word_count.get(word, 0) + 1

        for word in words2:
            word_count[word] = word_count.get(word, 0) + 1

        uncommon_words = [word for word in word_count if word_count[word] == 1]
        
        return uncommon_words

s1 = "this apple is sweet"
s2 = "this apple is sour"
solution = Solution()
print(solution.uncommonFromSentences(s1, s2))

s1 = "apple apple"
s2 = "banana"
print(solution.uncommonFromSentences(s1, s2))
