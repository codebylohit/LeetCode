class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_score = sorted(score, reverse=True)
        rank_map = {}
        for i, val in enumerate(sorted_score):
            rank_map[val] = medals[i] if i < 3 else str(i + 1)
        return [rank_map[s] for s in score]