def search(nums, target) :
        
    # linear search - O(n)
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False
    """

    # * Binary Search - O(log n)
    # To perform the binary search the array must be sorted first
    
    left, right = 0, len(nums) - 1
    
    while left <= right:  # here equal sign is needed for the case where nums have single element
        
        middle = (left + right) // 2
        
        if nums[middle] == target: return middle
        
        if nums[middle] < target:
            left = middle + 1
        
        else:
            right = middle - 1
        
    return -1
    
    



    

    
print(search([-1,0,3,5,9,12], 9))