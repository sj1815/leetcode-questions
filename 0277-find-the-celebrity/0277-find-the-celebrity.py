# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for person in range(1,n):
            res = knows(candidate, person)
            if res:
                candidate = person

        for person in range(n):
            if person == candidate:
                continue
            if knows(candidate, person) or not knows(person, candidate):
                return -1

        return candidate