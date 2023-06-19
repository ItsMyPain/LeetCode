from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        f = 0
        s = len(height) - 1
        v = 0

        while f < s:
            v = max(v, (s - f) * min(height[s], height[f]))

            if height[f] < height[s]:
                f += 1
            elif height[f] > height[s]:
                s -= 1
            else:
                f += 1
                s -= 1

        return v
