class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotatingNos = {
            "0": "0", 
            "1": "1",
            "8": "8",
            "6": "9",
            "9": "6",
            }
        rotatedNo = []

        for ch in str(n):
            if ch not in rotatingNos:
                return False
            rotatedNo.append(rotatingNos[ch])

        rotatedNo = "".join(rotatedNo)

        return int(rotatedNo[::-1]) != n
            
