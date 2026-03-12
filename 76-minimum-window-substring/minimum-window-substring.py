class Solution:
    def minWindow(self, s: str, t: str) -> str:  
        need = Counter(t)          # characters required
        missing = len(t)           # how many characters still needed
        left = start = end = 0     # window pointers

        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # when window satisfies t
            if missing == 0:
                # move left to shrink window
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # update minimum window
                if end == 0 or right - left < end - start:
                    start, end = left, right

                # move left forward to search next window
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end] 