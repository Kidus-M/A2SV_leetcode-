class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = {0}
        visited = set()
        while keys:
            new_keys = set()
            for i in keys :
                visited.add(i)
                new_keys.update(rooms[i])
            keys = new_keys - visited
        return len(visited) == len(rooms)