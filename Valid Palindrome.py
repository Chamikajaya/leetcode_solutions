"""  
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
"""


def isPalindrome(str):
    left = 0
    right = len(str) - 1
    
    str = str.lower()
    
    while left <= right:
        
        while left < len(str) and not str[left].isalnum():  # increment left pointer till we find a alpha numeric character, but left < len(str) should be checked otherwise left pointer will go beyond the length of the string
            left += 1
        
        while right > -1 and  not str[right].isalnum():
            right -= 1
        
        if left < right and  str[left] != str[right]:  # here first check left < right is needed for strings like ";;;;" where left and right will be beyond the end and start of the string, in which case this will generate an index out of range error. So to prevent that from happening first check is needed
            print(False)
            return False
        
        left += 1
        right -= 1
        
        
    print(True)
    return True
        
        

isPalindrome("A man, a plan, a canal: Panama")
    