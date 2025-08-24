class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        seen = {0: -1}
        state = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                state ^= 1 << vowel_to_bit[char]
            if state in seen:
                max_length = max(max_length, i - seen[state])
            else:
                seen[state] = i

        return max_length