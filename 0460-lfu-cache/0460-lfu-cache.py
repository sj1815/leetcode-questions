class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        self.key_to_val_freq = {}              # key -> (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys


    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        value, freq = self.key_to_val_freq[key]

        # Remove key from current freq
        del self.freq_to_keys[freq][key]

        # If this freq was min_freq and is now empty, increase min_freq
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1

        # Add key to next freq
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (value, freq + 1)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            # Update value and frequency
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)   # reuse get to update freq
            return

        # If cache is full → evict LFU
        if self.size == self.capacity:
            # Evict LRU key from min_freq
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
            self.size -= 1

        # Insert new key with freq = 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)