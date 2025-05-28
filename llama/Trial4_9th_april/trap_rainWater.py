class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers at both ends of the elevation map
        left, right = 0, len(height) - 1

        # Initialize variables to keep track of maximum heights on both sides
        max_left, max_right = 0, 0

        # Initialize variable to store the total trapped water
        total_water = 0

        while left <= right:
            # If the height at the left pointer is less than the height at the right pointer,
            # we move the left pointer to the right and update max_left if necessary.
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            # Otherwise, we move the right pointer to the left and update max_right if necessary.
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1

        return total_water