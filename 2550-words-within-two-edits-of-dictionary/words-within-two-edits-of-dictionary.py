class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        n = len(queries[-1])

        def isValid(query, element):
            count = 0
            for i in range(n):
                if query[i] != element[i]:
                    count += 1
                    if count > 2:
                        return False
            return count <= 2

        for query in queries:
            for element in dictionary:
                if isValid(query, element):
                    result.append(query)
                    break
        return result