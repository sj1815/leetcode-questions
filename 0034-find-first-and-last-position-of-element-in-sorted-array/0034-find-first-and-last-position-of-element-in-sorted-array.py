class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1 
                if nums[mid] == target:
                    index = mid
            return index

        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1 
                if nums[mid] == target:
                    index = mid
            return index




        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)
        return [left_index, right_index]