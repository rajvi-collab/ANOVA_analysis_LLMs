class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left = 0
        right = len(height) - 1
        max_left_height = 0
        max_right_height = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] >= max_left_height:
                    max_left_height = height[left]
                else:
                    total_water += max_left_height - height[left]
                left += 1
            else:
                if height[right] >= max_right_height:
                    max_right_height = height[right]
                else:
                    total_water += max_right_height - height[right]
                right -= 1
        return total_water