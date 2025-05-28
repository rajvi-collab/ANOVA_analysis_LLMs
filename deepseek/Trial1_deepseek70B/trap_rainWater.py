# Attempt 1st ======================
# 324 / 324 testcases passed

def trap_rain_water(heights):
    if not heights:
        return 0

    left = 0
    right = len(heights) - 1
    left_max = heights[left]
    right_max = heights[right]

    result = 0

    while left < right:
        if left_max < right_max:
            left += 1
            if heights[left] < left_max:
                result += left_max - heights[left]
            else:
                left_max = heights[left]
        else:
            right -= 1
            if heights[right] < right_max:
                result += right_max - heights[right]
            else:
                right_max = heights[right]

    return result

# Example usage:
heights = [4,2,0,3,2,5]
print(trap_rain_water(heights))  # Output: 9