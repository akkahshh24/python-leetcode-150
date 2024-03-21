class Solution:
    def isValid(self, s: str) -> bool:
        # Last bracket in, first bracket out
        # Use stacks

        # # Solution 1:
        # stack = []
        # bracket_pairs = {"{":"}", "(":")", "[":"]"}

        # for b in s:
        #     # opening bracket, add it to the stack
        #     if b in bracket_pairs.keys():
        #         stack.append(b)
        #     # closing bracket
        #     else:
        #         # if stack is empty
        #         if not stack or bracket_pairs[stack[-1]] != b:
        #             return False
        #         stack.pop()

        # return True if not stack else False
    
        # Solution 2:
        while True:
            old_len = len(s)

            s = s.replace("{}", "").replace("[]", "").replace("()", "")

            new_len = len(s)

            if new_len == old_len:
                break

        return len(s) == 0