def isAnagram(s,t):
    
    # early return if lengths are not the same
    if len(s) != len(t):
        return False    

    char_counter = dict()
    
    for i in range(len(s)):
        
        # we use get method so that even if the element does not exist we can return a default val of 0
        char_counter[s[i]] = char_counter.get(s[i], 0) + 1
        char_counter[t[i]] = char_counter.get(t[i], 0) - 1
        
    return all([count == 0 for count in char_counter.values])  # Creates a list of boolean vals and if each element is True I will return True
        
        
    
    