class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            while ans and math.gcd(ans[-1], num) > 1:
                curr = ans.pop()
                num = (curr * num) // math.gcd(curr, num)
            
            ans.append(num)
        
        return ans

        