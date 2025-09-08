class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        listik = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        copy = sorted(score, reverse=True)
        mapp = {}
        res = []

        for i in range(len(score)):
            if i <= 2:
                mapp[copy[i]] = listik[i]
            else:
                mapp[copy[i]] = str(i + 1)

        for i in score:
            res.append(mapp[i])

        return res