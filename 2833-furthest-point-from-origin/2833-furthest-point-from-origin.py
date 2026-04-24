class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = R = Dash = 0
        for i in moves:
            if i == "L":
                L += 1
            elif i == "R":
                R += 1
            else:
                Dash += 1
        return abs(L - R) + Dash