class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []

        def remove(s, last_i, last_j, par):
            bal = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    bal += 1
                elif s[i] == par[1]:
                    bal -= 1
                if bal >= 0:
                    continue
                for j in range(last_j, i + 1):
                    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                        remove(s[:j] + s[j + 1:], i, j, par)
                return
            rev = s[::-1]
            if par[0] == '(':
                remove(rev, 0, 0, [')', '('])
            else:
                res.append(rev)

        remove(s, 0, 0, ['(', ')'])
        return res 