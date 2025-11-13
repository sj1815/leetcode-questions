class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        curr = 1

        for num in target:
            while curr < num:
                res.append("Push")
                res.append("Pop")
                curr += 1
            res.append("Push")
            curr += 1
        
        return res
            