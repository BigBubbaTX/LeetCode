class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1 or s[0] == ")" or s[0] == "}"or s[0] == "]":
            return False
      
        for i in range(0,len(s)):
            current = s[i] 
            c = 1
            #print(f"stack is { stack} stack total {len(stack)} current is {current}")
            if current == "(":
                stack.append(s[i])
                c = 0
            elif current == "[":
                stack.append(s[i])
                c = 0
            elif current == "{":
                stack.append(s[i])
                c = 0
            if c == 1:
                try:
                     thing = stack.pop()
                except IndexError:
                    return False
                
                if thing == "(" and current != ")":
                    return False
                elif thing == "[" and current != "]":
                    return False
                elif thing == "{" and current != "}":
                    return False
            if i == len(s)-1 and len(stack) != 0:
                return False

        return True
        