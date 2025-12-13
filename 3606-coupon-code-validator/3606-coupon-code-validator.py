class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        priority = {
            "electronics" : 0,
            "grocery" : 1,
            "pharmacy" : 2,
            "restaurant" : 3
        }

        validCoupans = []

        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue

            if b not in priority:
                continue
            
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue
            
            validCoupans.append((priority[b], c))

        validCoupans.sort()
        
        return [c for _, c in validCoupans]