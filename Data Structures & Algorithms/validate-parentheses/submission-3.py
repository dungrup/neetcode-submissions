class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')':'(', '}':'{', ']':'['}
        my_stack = []

        for itm in s:
            if itm in my_dict:
                if my_stack and my_stack[-1] == my_dict[itm]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(itm)


        return False if my_stack else True
