class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            print("false")

        number = str(x)
        if number == number[::-1]:
            return True
        else:
            return False