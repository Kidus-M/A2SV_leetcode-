class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def comb(arr):
            if(len(arr) in [0,1,2]):
                return 1
            root = arr[0]
            left = []
            right = []
            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)
            ans = math.comb(len(arr)-1,len(left))
            leff = comb(left)
            righ = comb(right)
            return (leff*righ*ans)%1000000007
        anss = (comb(nums))
        return anss-1
        