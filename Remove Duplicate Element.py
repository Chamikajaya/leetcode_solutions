def x(nums):
       
    #    given that the array is already sorted
    
    slow = 0
    
    for fast in range(len(nums)):
        
        if nums[slow] != nums[fast]:
            slow += 1  #  increment slow pointer firstly
            nums[slow] = nums[fast]
    
    print(nums)
    print(slow + 1)    
    return slow + 1  # make sure to increment 1, as slow is the index and in question they ask for the length
            
   
        
    
                
            
            
        
        
        
        
print(x([2,2,3,3,4]))