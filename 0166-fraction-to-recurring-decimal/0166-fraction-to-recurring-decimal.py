class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator  == 0:
            return "0"
        
        res = []

        if (numerator > 0) != (denominator > 0):
            res.append("-")
        
        n, d = abs(numerator), abs(denominator)

        integer = n // d
        res.append(str(integer))

        remainder = n % d
        if remainder == 0:
            return "".join(res)
        
        res.append(".")
        rem_map = {}

        while remainder != 0:
            if remainder in rem_map:
                si = rem_map[remainder]
                res.insert(si, "(")
                res.append(")")
                break
            rem_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // d))
            remainder %= d

        return "".join(res)

        