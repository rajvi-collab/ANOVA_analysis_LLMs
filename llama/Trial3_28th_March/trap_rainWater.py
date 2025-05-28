class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize variables to store total trapped water and pointers
        total_water = 0
        left = 0
        right = len(height) - 1

        # Initialize maximum heights for the left and right pointers
        max_left_height = 0
        max_right_height = 0

        while left <= right:
            # If the height at the left pointer is less than the height at the right pointer,
            # update the maximum left height if necessary, calculate trapped water, and move the left pointer to theright.
            if height[left] < height[right]:
                if height[left] >= max_left_height:
                    max_left_height = height[left]
                else:
                    total_water += max_left_height - height[left]
                left += 1
            # If the height at the right pointer is less than or equal to the height at the left pointer,
            # update the maximum right height if necessary, calculate trapped water, and move the right pointer to the left.
            else:
                if height[right] >= max_right_height:
                    max_right_height = height[right]
                else:
                    total_water += max_right_height - height[right]
                right -= 1

        return total_water