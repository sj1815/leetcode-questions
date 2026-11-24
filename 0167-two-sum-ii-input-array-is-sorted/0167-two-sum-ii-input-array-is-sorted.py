class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) - 1

        while l < h:
            sum = numbers[l] + numbers[h]

            if sum == target:
                return [l+1, h+1]
            elif sum < target:
                l += 1
            else:
                h -= 1

        return [-1, -1]        