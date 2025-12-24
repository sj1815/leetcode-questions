class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum_of_apples = sum(apple)
        capacity.sort(reverse=True)
        res = 0

        curr_capacity = 0
        boxes = 0

        for cap in capacity:
            curr_capacity += cap
            boxes += 1
            if curr_capacity >= sum_of_apples:
                return boxes

        return boxes