class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_day(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days[:month - 1]) + day

        start = max(get_day(arriveAlice), get_day(arriveBob))
        end = min(get_day(leaveAlice), get_day(leaveBob))

        return max(0, end - start + 1)