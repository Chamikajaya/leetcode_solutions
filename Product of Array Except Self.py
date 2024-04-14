def productExceptSelf(nums):
    
    # * My initial solution --> O(n) but space is also O(n)
    
    
    # TODO:- Solve with constant space
    
    
    
    
    
    size = len(nums)
    left_prod_array = [1] * size  # first element of nums will have left prod of 1
    right_prod_array = [1] * size  # last element of nums will have right prod of also 1
    
    for i in range(1,size):
        left_prod_array[i] = nums[i-1] * left_prod_array[i-1]
        right_prod_array[size-i-1] = nums[size-i] * right_prod_array[size-i]
    
    # for j in range(size - 2, -1,-1):
    #     right_prod_array[j] = nums[j+1] * right_prod_array[j+1]
        
    result = [i * j for i, j in zip(left_prod_array, right_prod_array)]
    
    print(result) 
        
    
    
    

productExceptSelf([1,2,3,4])