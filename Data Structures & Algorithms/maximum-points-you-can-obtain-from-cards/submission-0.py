class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        l = 0
        r = k - 1
        count = 0
        prev_sum = sum(cardPoints[l : r + 1])
        max_score = prev_sum
        while count < k:
            prev_sum -= cardPoints[r]
            r -= 1
            l -= 1
            prev_sum += cardPoints[l]
            max_score = max(max_score, prev_sum)
            count += 1
        return max_score
