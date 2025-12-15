class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        ends = [job[1] for job in jobs]

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            # Option 1: skip current job
            skip = dp[i - 1]

            # Option 2: take current job
            take = jobs[i][2]
            start = jobs[i][0]

            # Find last job that ends <= start
            j = bisect_right(ends, start) - 1
            if j >= 0:
                take += dp[j]

            dp[i] = max(skip, take)

        return dp[-1]