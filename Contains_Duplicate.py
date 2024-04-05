from collections import defaultdict

def containsDuplicate(nums):
    
    counter_dict = dict()
    
    for i in range(len(nums)):
       
       if nums[i] not in counter_dict:
           counter_dict[nums[i]] = 1
       else:
           return True
           
    
    
    return False