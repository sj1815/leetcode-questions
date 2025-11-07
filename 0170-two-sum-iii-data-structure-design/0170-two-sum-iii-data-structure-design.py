class TwoSum:

    def __init__(self):
        self.num_count = {}
        
    def add(self, number: int) -> None:
        self.num_count[number] = self.num_count.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.num_count:
            complement = value - num
            if complement in self.num_count:
                if complement != num or self.num_count[num] > 1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)