class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(openP, closeP, brack):
            if openP == closeP == n:
                ans.append(brack)
                return
            if openP < n:
                generate(openP + 1, closeP, brack + "(")
            if closeP < openP:
                generate(openP, closeP + 1, brack + ")")
        
        ans = []
        generate(0, 0, "")
        return ans