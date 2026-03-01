from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        flat_array = [col for row in mat for col in row]
        if len(flat_array) != r * c: 
            return mat
        
        return [flat_array[i*c:c*(i+1)] for i in range(r)]


if __name__ == "__main__":
    solution = Solution()
    mat = [[1, 2], [3, 4]]
    print(solution.matrixReshape(mat, 1, 4))