class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []

        def backtrack(index, target, curr):
            if target == 0:
                ans.append(curr[:])
                return
            if index == len(candidates) or target < 0:
                return

            curr.append(candidates[index])
            backtrack(index, target - candidates[index], curr)
            curr.pop()


            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            backtrack(next_index, target, curr)

        backtrack(0, target, [])
        return ans