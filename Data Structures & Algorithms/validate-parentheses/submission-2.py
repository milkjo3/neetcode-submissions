class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []

        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            elif stack == []:
                return False
            elif bracket == ")" and stack[-1] != "(":
                return False
            elif bracket == "]" and stack[-1] != "[":
                return False
            elif bracket == "}" and stack[-1] != "{":
                return False
            else:
                stack.pop()
        return True if stack == [] else False