class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            for s in dictionary:
                dis = 0
                for i in range(len(query)):
                    if query[i] != s[i]:
                        dis += 1
                if dis <= 2:
                    ans.append(query)
                    break
        return ans