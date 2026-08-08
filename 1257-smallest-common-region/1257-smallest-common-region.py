class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}

        for region in regions:
            root = region[0]
            for child in region[1:]:
                parent[child] = root

        ancestors = set()
        while region1:
            ancestors.add(region1)
            region1 = parent.get(region1)

        while region2 not in ancestors:
            region2 = parent.get(region2)

        return region2