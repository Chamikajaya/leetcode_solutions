def twoSum(nums, target):
    
    needed_and_index_dict = dict()  # required val : index
    
    for i in range(len(nums)):
        
        if nums[i] in needed_and_index_dict:
            return [i, needed_and_index_dict[nums[i]]]
        else:
            need_val_to_get_target = target - nums[i]
            needed_and_index_dict[need_val_to_get_target] = i
        
        # no need for further checks coz we are given that one valid answer exists.
        

print(twoSum([2,7,11,15], 9))