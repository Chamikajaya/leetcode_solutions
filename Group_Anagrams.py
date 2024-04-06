# """
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# """

from collections import defaultdict

def groupAnagrams(strs):
    
    dict_holder = dict()  # This dict will hold the sorted word as key and corresponding anagrams list as values
    
    
    for word in strs:
        
        sorted_word = "".join(sorted(word))  # Sorted word will be the key since all anagrams will be the same after sorting
        
        if sorted_word not in dict_holder:
            dict_holder[sorted_word] = [word]
        else:
            dict_holder[sorted_word].append(word)
    
    # print(dict_holder)
    
    return list(dict_holder.values())  # Now simply print the dict's values :)
        
        
       
    
groupAnagrams(["eat","tea","tan","ate","nat","bat"])
                
            
            
            
            
# x = "fdkzf"
# print("".join(sorted(x)))