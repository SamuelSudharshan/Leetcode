class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={')':'(', ']':'[','}':'{'}
        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in ']})':
                if not stack or map[i] != stack[-1]:
                    return False
                stack.pop()
        return len(stack)==0