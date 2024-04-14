
def sortedSquares(nums):
    
    # * We are given that nums array is sorted in ascending order
    
    left, right = 0, len(nums) - 1
    squares_sorted = [0] * len(nums)
    position = right
    
    while right >= left:
        if abs(nums[left]) <= abs(nums[right]):
            squares_sorted[position] = nums[right] ** 2
            right -= 1
        else:
            squares_sorted[position] = nums[left] ** 2
            left += 1
        position -= 1
    
    print(squares_sorted)

            


sortedSquares([-4,-1,0,3,10])