# """
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# """

from collections import defaultdict

# a - 97 || z - 122
def groupAnagrams(strs):
    
    # * Time -> O (n k log k ) ; n - num of strings || k - num of chars per string
    """
    dict_holder = dict()  # This dict will hold the sorted word as key and corresponding anagrams list as values
    
    
    for word in strs: 
        
        sorted_word = "".join(sorted(word))  # Sorted word will be the key since all anagrams will be the same after sorting
        
        if sorted_word not in dict_holder:
            dict_holder[sorted_word] = [word]
        else:
            dict_holder[sorted_word].append(word)
    
    # print(dict_holder)
    
    return list(dict_holder.values())  # Now simply print the dict's values :)
    """

    # * Better time complexity -> O (n * k)
    # The following approach is valid as we are given that each string has only lowercase letters
    my_dict = defaultdict(list)
    
    for word in strs:
        boolean_mask = [0] * 26
        
        for i in range(len(word)):
            corresponding_idx = ord(word[i]) - 97  # 97 = ord("a")
            boolean_mask[corresponding_idx] += 1  # incrementing is need for cases like ["abbbb", "baaa"] 🥹
        
        my_dict[tuple(boolean_mask)].append(word)  # make sure to convert the list to tuple as dict can not contain lists as their keys
        
    return my_dict.values()
            
        
    
    
    
    
    
       
    
groupAnagrams(["eat","tea","tan","ate","nat","bat"])
                
            
            
            
            
# x = "fdkzf"
# print("".join(sorted(x)))