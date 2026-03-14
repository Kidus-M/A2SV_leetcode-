class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.answer = ""

        def backtrack(curr: list[str]) -> None:
            if self.answer:
                return

            if len(curr) == n:
                self.count += 1
                if self.count == k:
                    self.answer = "".join(curr)
                return

            for ch in ['a', 'b', 'c']:
                if curr and curr[-1] == ch:
                    continue

                curr.append(ch)
                backtrack(curr)
                curr.pop()

        backtrack([])
        return self.answer