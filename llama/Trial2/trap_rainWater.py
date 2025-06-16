from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                water += max_left - height[left]
                left += 1
            else:
                water += max_right - height[right]
                right -= 1
        return water


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    # Output: 6

    print(solution.trap([4,2,0,3,2,5]))
    # Output: 9