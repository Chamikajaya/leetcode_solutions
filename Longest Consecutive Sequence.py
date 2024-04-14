"""
When we consider [100,4,200,1,3,2] , we can see that there exists 3 sequences
1,2,3,4 ......  100 ......  200

The start of a sequence is determined by when (n-1) number does not exist

"""


def longestConsecutive(nums):
    
    
    for number in nums:
        left_side_num = number - 1
        if left_side_num not in nums:
            curr_sequence_len = 1
            right_side_num = number + 1
            while True:
                if right_side_num in nums:
                    curr_sequence_len += 1
                    right_side_num += 1
                else:
                    max_len_sequence = max(max_len_sequence, curr_sequence_len)
                    break

    
                    
    
    
    
    
    


longestConsecutive([100,4,200,1,3,2])