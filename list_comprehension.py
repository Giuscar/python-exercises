""""
You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer m. Print a list
of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k  is not equal to n.
Here, 0 <= i <= x, 0 <= j <= y, 0 <= k <= z.
"""
def print_list_combinations(x, y, z, n):
    print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k != n])

if __name__ == "__main__":
    print_list_combinations(1, 1, 1, 2)