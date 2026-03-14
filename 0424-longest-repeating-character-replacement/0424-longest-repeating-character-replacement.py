class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        count, left, max_freq = 0,0,0

        for right in range(len(s)):
            char_counts[s[right]] = 1 + char_counts.get(s[right], 0)
            if char_counts[s[right]] > max_freq:
                max_freq = char_counts[s[right]]
            
            while right - left + 1 - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1
            count = max(count, right-left + 1)

        return count