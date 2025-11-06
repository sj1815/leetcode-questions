class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_no = float('inf')
        second_no = float('inf')

        for num in nums:
            if num <= first_no:
                first_no = num
            elif num <= second_no:
                second_no = num
            else:
                return True
        
        return False
        