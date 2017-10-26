class solution:
    def isValid(self, s):

        left_sign = ["{","[","("]
        right_sign = ["}","]",")"]
        sing_pair = {
                        ")":"(",
                        "}":"{",
                        "]":"["
                    }
        stack = []
        for i in range(len(s)):

            if s[i] in left_sign:
                stack.append(s[i])
            elif s[i] in right_sign:
                if sing_pair[s[i]] == stack[-1]:
                    del stack[-1]
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                    
        
        
    

s = solution()
print(s.isValid("{}([)][]"))
        
