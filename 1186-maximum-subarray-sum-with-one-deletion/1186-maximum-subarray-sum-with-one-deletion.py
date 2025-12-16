class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]
        one_del = 0
        ans = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            one_del = max(one_del + x, no_del)
            no_del = max(no_del + x, x)

            ans = max(ans, no_del, one_del)

        return ans