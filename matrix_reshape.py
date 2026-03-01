from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        flat_array = [col for row in mat for col in row]
        if len(flat_array) != r * c: 
            return mat
        
        return [flat_array[i*c:c*(i+1)] for i in range(r)]


# Unit Tests
import unittest

class TestMatrixReshape(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_valid_reshape_2x4_to_4x2(self):
        """Test reshaping a 2x4 matrix to 4x2"""
        mat = [[1, 2], [3, 4]]
        result = self.solution.matrixReshape(mat, 4, 2)
        expected = [[1], [2], [3], [4]]
        self.assertEqual(result, expected)
    
    def test_valid_reshape_2x2_to_1x4(self):
        """Test reshaping a 2x2 matrix to 1x4"""
        mat = [[1, 2], [3, 4]]
        result = self.solution.matrixReshape(mat, 1, 4)
        expected = [[1, 2, 3, 4]]
        self.assertEqual(result, expected)
    
    def test_invalid_reshape_returns_original(self):
        """Test that invalid reshape returns original matrix"""
        mat = [[1, 2], [3, 4]]
        result = self.solution.matrixReshape(mat, 2, 3)
        self.assertEqual(result, mat)
    
    def test_reshape_single_row_to_multiple_rows(self):
        """Test reshaping a single row to multiple rows"""
        mat = [[1, 2, 3, 4, 5, 6]]
        result = self.solution.matrixReshape(mat, 2, 3)
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected)
    
    def test_reshape_multiple_rows_to_single_row(self):
        """Test reshaping multiple rows to a single row"""
        mat = [[1, 2], [3, 4], [5, 6]]
        result = self.solution.matrixReshape(mat, 1, 6)
        expected = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(result, expected)
    
    def test_reshape_3x3_to_9x1(self):
        """Test reshaping a 3x3 matrix to 9x1"""
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.matrixReshape(mat, 9, 1)
        expected = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()