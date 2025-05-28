# Attempt 1st ======================
# 3 / 324 testcases passed
class Solution:
    def trap(self, height):
        if not height or len(height) < 3:
            return 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        # Initialize max values for each index from the beginning and end.
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        for i in reversed(range(len(height)-1)):
            right_max[i] = max(right_max[i+1], height[i])

        # For each index, the amount of trapped water is min(left_max, right_max) - current height.
        return sum(min(l, r) - h for l, r, h in zip(left_max, right_max, height)) - sum(height)

# Attempt another ===============
# 324 / 324 testcases passed - removed constrained

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]

        while left < right:
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
                l_max = max(l_max, height[left])

            else:
                volume += r_max - height[right]
                right -= 1
                r_max = max(r_max, height[right])

        return volume

