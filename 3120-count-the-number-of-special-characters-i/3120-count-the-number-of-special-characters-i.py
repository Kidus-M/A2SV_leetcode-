class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letter_counter = [-1]*26
        result = 0
        for c in word:
            if c.islower():
                idx = ord(c) - ord('a')
                if letter_counter[idx] == -1:
                    letter_counter[idx] = 1
                elif letter_counter[idx] == 2:
                    letter_counter[idx] = 3
                    result += 1
            elif c.isupper():
                idx = ord(c) - ord('A')
                if letter_counter[idx] == -1:
                    letter_counter[idx] = 2
                elif letter_counter[idx] == 1:
                    letter_counter[idx] = 3
                    result += 1

        return result