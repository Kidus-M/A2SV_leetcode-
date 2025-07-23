class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            for ii in range(i+1, len(s)+1):
                if all(s[k].swapcase() in s[i:ii] for k in range(i, ii)):
                    ans = max(ans, s[i:ii], key=len)
        return ans