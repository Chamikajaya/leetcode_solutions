
# should be inplace 
"""
first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):

            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow  # simply return slow as they do not care about the content of the list
