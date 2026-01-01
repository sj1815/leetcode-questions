class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def addOne(d):
            if len(d) == 0:
                return [1]
            new_dig = d.pop() + 1
            if new_dig == 10:
                d = addOne(d)
                new_dig = 0
            d.append(new_dig)
            return d
            
        return addOne(digits)