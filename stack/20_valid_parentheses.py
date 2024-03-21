class Solution:
    def isValid(self, s: str) -> bool:
        # Last bracket in, first bracket out
        # Use stacks

        stack = []
        bracket_pairs = {"{":"}", "(":")", "[":"]"}

        for b in s:
            # opening bracket, add it to the stack
            if b in bracket_pairs.keys():
                stack.append(b)
            # closing bracket
            else:
                # if stack is empty
                if not stack or bracket_pairs[stack[-1]] != b:
                    return False
                stack.pop()

        return True if not stack else False