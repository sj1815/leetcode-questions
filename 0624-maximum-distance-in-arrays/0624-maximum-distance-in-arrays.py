class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arr = arrays[0][0]
        max_arr = arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            ans = max(
                ans,
                abs(curr_max - min_arr),
                abs(max_arr - curr_min)
            )

            min_arr = min(min_arr, curr_min)
            max_arr = max(max_arr, curr_max)

        return ans
        