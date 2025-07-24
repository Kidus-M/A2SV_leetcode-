class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        tree = defaultdict(list)

        for emp in range(n):
            if manager[emp] != -1:
                tree[manager[emp]].append(emp)

        def dfs(emp_id):
            if emp_id not in tree:
                return 0
            max_time = 0
            for sub in tree[emp_id]:
                max_time = max(max_time, dfs(sub))
            return informTime[emp_id] + max_time

        return dfs(headID)