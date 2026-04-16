class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        num_pos = defaultdict(list)

        for i in range(n):
            num_pos[nums[i]].append(i)

        for pos in num_pos.values():
            x = pos[0]
            pos.insert(0, pos[-1] - n)
            pos.append(x + n)

        for i in range(len(queries)):
            x = nums[queries[i]]
            pos_list = num_pos[x]
            if len(pos_list) == 3:
                queries[i] = -1
                continue
            pos = bisect.bisect_left(pos_list, queries[i])
            queries[i] = min(
                pos_list[pos + 1] - pos_list[pos],
                pos_list[pos] - pos_list[pos - 1],
            )

        return queries