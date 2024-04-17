class Solution:
    def isValid(self, s: str) -> bool:

        # odd length strings will never be valid
        if len(s) % 2 ==  1: return False 

        my_map = {")":"(", "}":"{", "]":"["}

        stack = []


        for i in range(len(s)):

            # push to the stack if it is an opening bracket
            if s[i] not in my_map:
                stack.append(s[i])
            else:
                if stack and stack[-1] == my_map[s[i]]:
                    stack.pop()
                else:
                    return False
        
        # check whether the stack is empty , if empty string is valid
        if stack:
            return False
        else:
            return True
        