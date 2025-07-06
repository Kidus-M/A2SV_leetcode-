class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hLen = len(haystack)
        nLen = len(needle)

        if nLen == 0:
            return 0

        i = 0
        while i < hLen:
            nIndex = 0
            j = i

            while j < hLen and nIndex < nLen and haystack[j] == needle[nIndex]:
                j += 1
                nIndex += 1

            if nIndex == nLen:
                return i

            i += 1

        return -1