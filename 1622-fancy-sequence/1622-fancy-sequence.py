class Fancy:
    def __init__(self):
        self.arr = []
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        inv = pow(self.mult, self.MOD-2, self.MOD)
        val = (val - self.add) % self.MOD
        val = (val * inv) % self.MOD
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        
        val = self.arr[idx]
        return (val * self.mult + self.add) % self.MOD
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)