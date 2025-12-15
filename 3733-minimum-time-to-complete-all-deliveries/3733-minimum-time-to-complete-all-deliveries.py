class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        lo, hi = 0, 10**18  
        lcm_val = math.lcm(r[0], r[1])
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            avail1 = mid - (mid // r[0])
            avail2 = mid - (mid // r[1])
            totAvail = mid - (mid // lcm_val)
            
            if avail1 >= d[0] and avail2 >= d[1] and totAvail >= d[0] + d[1]:
                hi = mid
            else:
                lo = mid + 1
        
        return lo