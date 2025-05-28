# Attempt 4th =====================

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize variables to store the total trapped water and the left and right pointers
        total_water = 0
        left = 0
        right = len(height) - 1

        # Initialize variables to store the maximum heights on the left and right sides
        max_left = 0
        max_right = 0

        # Iterate through the elevation map from both ends
        while left <= right:
            # Update the maximum heights on the left and right sides
            if height[left] < height[right]:
                # If the current height on the left is less than the maximum height on the left,
                # update the total trapped water and move the left pointer to the right
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                # If the current height on the right is less than or equal to the maximum height on the right,
                # update the total trapped water and move the right pointer to the left
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1

        return total_water