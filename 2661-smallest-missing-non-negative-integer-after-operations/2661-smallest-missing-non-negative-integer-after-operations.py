class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        N = len(nums)
        mods = [0]*value

        for num in nums:
            mods[num%value] += 1
        
        curr_val = 0
        while curr_val < N:
            if not mods[curr_val%value]:
                return curr_val
            mods[curr_val%value] -= 1
            curr_val += 1
        
        return curr_val
        