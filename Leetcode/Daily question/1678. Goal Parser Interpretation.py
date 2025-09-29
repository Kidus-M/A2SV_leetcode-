class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans=""
        start=0
        curr=""
        for end in range(len(command)):
            curr += command[end]
            if curr == 'G':
                ans += 'G'
                curr = ""
                start = end +1
            elif curr =="()":
                ans += "o"
                curr =""
                start =end +1
            elif curr == "(al)":
                ans += "al"
                curr=""
                start = end +1
        return ans