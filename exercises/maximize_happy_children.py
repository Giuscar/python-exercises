from typing import List


class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_happiness_sum = 0
        turns = 0
        for i in range(k):
            total_happiness_sum += max(happiness[i] - turns, 0)
            turns += 1

        return total_happiness_sum


if __name__ == "__main__":
    max_happiness = Solution().maximumHappinessSum([10, 47, 47], 3)
    print(f"Max happiness is {str(max_happiness)}")
