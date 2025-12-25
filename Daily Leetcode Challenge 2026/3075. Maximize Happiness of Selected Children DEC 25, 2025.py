class Solution:
    def maximumHappinessSum(self, christmasJoy: List[int], k: int) -> int:
        christmasJoy.sort(reverse=True)

        totalJoy = 0
        for turn in range(k):
            currentJoy = christmasJoy[turn] - turn
            if currentJoy <= 0:
                break
            totalJoy += currentJoy
        return totalJoy