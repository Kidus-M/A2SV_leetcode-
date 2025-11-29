from collections import deque
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)

        if length < 3:
            return False

        decreasing_stack = deque()

        max_third_element = float('-inf')

        for i in range(length - 1, -1, -1):
            current_number = nums[i]

            if current_number < max_third_element:
                return True

            while decreasing_stack and decreasing_stack[0] < current_number:
                max_third_element = decreasing_stack.popleft()

            decreasing_stack.appendleft(current_number)

        return False