class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result.extend(matrix.pop(0))

            for i in range(len(matrix)):
                if matrix[i]:
                    result.append(matrix[i].pop(-1))
            
            if matrix:
                result.extend(matrix.pop(-1)[::-1])
            
            for i in range(len(matrix)-1, -1, -1):
                if matrix[i]:
                    result.append(matrix[i].pop(0))
        
        return result
        