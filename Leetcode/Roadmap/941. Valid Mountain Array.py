class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] < arr[left + 1]:
                left += 1
            elif arr[right - 1] > arr[right]:
                right -= 1
            else:
                break

        return ((left == right) and
                (left > 0 and right < len(arr) - 1))