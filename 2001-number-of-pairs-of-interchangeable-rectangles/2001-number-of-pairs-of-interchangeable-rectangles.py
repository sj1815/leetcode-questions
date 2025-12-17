class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_map = defaultdict(int)
        pairs = 0

        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)   # reduced ratio

            # count pairs formed with previous same ratios
            pairs += ratio_map[key]
            ratio_map[key] += 1

        return pairs