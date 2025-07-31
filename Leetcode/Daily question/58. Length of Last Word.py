class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            word_list = s.split()

            return len(word_list[-1])