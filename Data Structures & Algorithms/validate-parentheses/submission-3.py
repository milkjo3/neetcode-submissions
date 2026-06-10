class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {"(":")", "[":"]", "{":"}"}
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            elif not stack or bracket != mappings[stack[-1]]:
                return False    
            else:
                stack.pop()
        return not stack