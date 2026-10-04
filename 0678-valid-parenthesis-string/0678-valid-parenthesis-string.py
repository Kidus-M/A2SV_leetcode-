class Solution:
    def checkValidString(self, s: str) -> bool:
        mask = 1

        for ch in s:
            if ch == '(':
                mask = mask << 1
            elif ch == ')':
                mask = mask >> 1
            else:
                mask = (mask << 1) | mask | (mask >> 1)

            if mask == 0:
                return False

        return (mask & 1) != 0