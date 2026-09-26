class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')':'(', '}':'{', ']':'['}

        stack = deque()

        for item in s:
            if item in my_dict:
                if stack and my_dict[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        return True if not stack else False