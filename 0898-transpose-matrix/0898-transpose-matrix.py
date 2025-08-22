class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        ans = []
        for i in range(cols):
            temp = []
            for j in range(rows):
                temp.append(matrix[j][i])
            ans.append(temp)
        
        return ans
        