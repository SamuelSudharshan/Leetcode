class Solution:
    def calculate(self, s: str) -> int:
        num=0
        res=0
        sign=1
        stack=[]
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == '(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif i == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
            elif i in '+-':
                res += num * sign
                sign = 1 if i == '+' else -1
                num = 0
        return res + num * sign
