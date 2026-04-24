class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def is_valid(mid):
            day = 1
            weight = 0
            for i in weights:
                weight += i
                if weight > mid:
                    weight = i
                    day +=1

            return day <= days

        while low < high:   
            mid = (high+low)//2
            day = is_valid(mid)

            if day:
                high = mid
            else:
                low = mid + 1

        return low