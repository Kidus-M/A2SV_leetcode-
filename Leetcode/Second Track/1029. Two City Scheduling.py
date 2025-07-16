class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        totalA = 0
        for costA, _ in costs:
            totalA += costA
        difference = [costB-costA for costA, costB in costs]
        totalB = sum(sorted(difference)[:len(costs)//2])
        return totalA + totalB
