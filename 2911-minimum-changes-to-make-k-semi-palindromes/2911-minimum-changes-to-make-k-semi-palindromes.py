class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        width = n + 1
        INF = n + 1

        s = s.encode()
        cost = bytearray([255]) * (width * width)

        for d in range(1, n // 2 + 1):
            two_back = bytearray(width)
            one_back = bytearray(width)
            current = bytearray(width)

            for blocks in range(2, n // d + 1):
                length = blocks * d
                limit = n - length + 1

                for left in range(limit):
                    right = left + length

                    changes = two_back[left + d] if blocks >= 4 else 0

                    for offset in range(d):
                        changes += (
                            s[left + offset] !=
                            s[right - d + offset]
                        )

                    current[left] = changes

                    index = left * width + right
                    if changes < cost[index]:
                        cost[index] = changes

                two_back, one_back, current = (
                    one_back, current, two_back
                )

        previous = [INF] * width
        previous[0] = 0

        for pieces in range(1, k + 1):
            current_dp = [INF] * width

            for end in range(2 * pieces, width):
                best = INF

                for start in range(2 * (pieces - 1), end - 1):
                    candidate = (
                        previous[start] +
                        cost[start * width + end]
                    )

                    if candidate < best:
                        best = candidate

                current_dp[end] = best

            previous = current_dp

        return previous[n]