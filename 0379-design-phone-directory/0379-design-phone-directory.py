class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.is_slot_available = [True] * maxNumbers

    def get(self) -> int:
        index = next((i for i, available in enumerate(self.is_slot_available) if available), -1)
        if index != -1:
            self.is_slot_available[index] = False
        return index

    def check(self, number: int) -> bool:
        return self.is_slot_available[number]

    def release(self, number: int) -> None:
        self.is_slot_available[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)