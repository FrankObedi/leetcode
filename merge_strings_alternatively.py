class Solution:
    def mergeAlternatively(self, word1, word2):
        word1_len = len(word1)
        word2_len = len(word2)
        small_word = word1
        big_word = word2
        merged = []

        if word1_len > word2_len:
            small_word, big_word = word2, word1

        i = 0
        while i < len(small_word):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        
        while i < len(big_word):
            merged.append(big_word[i])
            i += 1
        
        return ''.join(merged)
    
s = Solution()
print(s.mergeAlternatively("frank","obedi"))
print(s.mergeAlternatively("ab","jklmn"))