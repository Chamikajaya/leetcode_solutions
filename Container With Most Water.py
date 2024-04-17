class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_container_size = 0

        while left < right:
            curr_container_size = (right - left) * min(height[left], height[right])

            max_container_size = max(max_container_size, curr_container_size)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_container_size