def topKFrequent(nums,k):
    
    my_counter = dict()
    
    index_matches_frequency_arr = [[] for _ in range(len(nums) + 1)]  #         # index_matches_frequency_arr array's index corresponds to the frequency 

    output = []
    
    for number in nums:
        if number not in my_counter:
            my_counter[number] = 1
        else:
            my_counter[number] += 1
            
    
    for num,freq in my_counter.items():
        index_matches_frequency_arr[freq].append(num)
        

    
    print(index_matches_frequency_arr)
    
    for i in range(len(index_matches_frequency_arr)-1, 0,-1):  
        
        for j in index_matches_frequency_arr[i]:
            output.append(j)
            
            if (len(output)) == k: return output
            
        
        
        
        

        
       




topKFrequent([4,1,-1,2,-1,2,3], 2)
# topKFrequent([1], 1)