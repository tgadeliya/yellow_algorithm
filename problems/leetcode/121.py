from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = [prices[0]]
        for i in range(1, len(prices)):
            mins.append(min([prices[i], mins[-1]]))

        maxs = [prices[-1]]
        for p in prices[::-1][1:]:
            maxs.append(max([p, maxs[-1]]))
        
        maxs = maxs[::-1]
        max_prof = float("-inf")
        for i in range(1, len(prices)):
            max_prof = max(max_prof, maxs[i] - mins[i-1])
        return max(0, max_prof)