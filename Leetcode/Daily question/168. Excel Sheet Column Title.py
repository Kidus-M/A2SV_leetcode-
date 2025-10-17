class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''
        columnNumber -= 1
        while columnNumber >= 0:
            columnNumber, rem = divmod(columnNumber, 26)
            ret = chr(rem + 65) + ret
            columnNumber -= 1
        return ret