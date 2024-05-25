class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        notMatch = []
        for i in range(len(expected)):
            if heights[i] != expected[i]:
                notMatch.append(expected[i])
        return len(notMatch)