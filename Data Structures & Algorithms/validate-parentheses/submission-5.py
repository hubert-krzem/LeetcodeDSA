class Solution:
    def isValid(self, s: str) -> bool:
        # Stack

        # 1. Every open bracket is closed by the same type of close bracket
        # 2. Open brackets are closed in the correct order
        # For last close bracket type, if open matches, pop, else return false

        # 3. Every close bracket has a corresponding open bracket of the same type
        # If reach end return stack == Empty

        brcktMap = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        stack = []
        for brckt in s:
            if brckt in brcktMap.keys():
                stack.append(brckt)
            else: # Close bracket
                # check if stack is non empty
                if stack and brcktMap[stack[-1]] == brckt:
                    stack.pop(-1)
                else:
                    return False

        return not stack