
# since the array is sorted we can use 2 pointers
def twoSum(numbers, target):
    
    left, right = 0, len(numbers) - 1
    
    while left < right:
        
        total = numbers[left] + numbers[right] 
        
        # problem says that the existence of sol is guaranteed
        if total == target:
            return [left+1, right+1]  # coz they have given 1 indexed arr 
        
        if total > target:
            right -= 1
        else:
            left += 1



print(twoSum([2,7,11,15], 9))