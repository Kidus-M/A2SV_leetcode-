class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = list(s)
        carry = 0


        while len(stack) != 1:
            curr = stack.pop()

            if curr == '0' and not carry:
                res += 1
            elif curr == '1' and not carry:
                carry =1
                res += 2
            elif curr=='0' and carry:
                res += 2
            else:
                res +=1
        if stack[0] == '1' and carry:
            res += 1

        return res
