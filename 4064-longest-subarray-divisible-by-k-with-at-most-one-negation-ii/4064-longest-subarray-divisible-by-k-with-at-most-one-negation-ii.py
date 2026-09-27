class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        map_no_neg = {0: -1}
        discovered = [(-1, 0)]

        min_L_for_combined = [float('inf')] * k
        last_seen = {}

        max_len = 0
        curr_sum = 0

        for j, num in enumerate(nums):

            curr_sum += num
            v = (2 * num) % k

            prev_j = last_seen.get(v, -1)

            start_idx = bisect.bisect_left(
                discovered,
                (prev_j, -1)
            )

            for idx, target_r in discovered[start_idx:]:

                if idx >= j:
                    break

                rem_combined = (target_r + v) % k

                if idx < min_L_for_combined[rem_combined]:
                    min_L_for_combined[rem_combined] = idx

            last_seen[v] = j

            rem = curr_sum % k

            if rem in map_no_neg:
                max_len = max(
                    max_len,
                    j - map_no_neg[rem]
                )
            else:
                map_no_neg[rem] = j
                discovered.append((j, rem))

            if min_L_for_combined[rem] != float('inf'):
                max_len = max(
                    max_len,
                    j - min_L_for_combined[rem]
                )

        return max_len