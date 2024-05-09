from collections import OrderedDict
from typing import List


class Solution:
    MAIN_SCORES = ["Gold Metal", "Silver Medal", "Bronze Medal"]

    def findRelativeRanks(self, scores: List[int]) -> List[str]:

        score_info = OrderedDict()
        output = []
        idx = 0
        for score in scores:
            score_info.update({score: {"idx": scores.index(score)}})

        ordered_scores = sorted(scores)

        for ordered_score in ordered_scores:
            if 0 <= idx < 3:
                score_info[ordered_score].update({"rank": self.MAIN_SCORES[idx]})
                idx += 1
            else:
                score_info[ordered_score].update({"rank": str(idx + 1)})
                idx += 1

        return [info["rank"] for _, info in score_info.items()]


if __name__ == "__main__":
    solution = Solution().findRelativeRanks([5, 4, 3, 2, 1])
