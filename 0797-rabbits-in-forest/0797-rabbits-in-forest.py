class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        min_rabbits = 0

        for a, b in freq.items():
            group_size = a + 1
            group = ceil(b / group_size)
            min_rabbits += group * group_size

        return min_rabbits        