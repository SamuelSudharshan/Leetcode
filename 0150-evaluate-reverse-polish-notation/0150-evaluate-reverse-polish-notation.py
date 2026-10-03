class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st=[]
        for i in tokens:
            if i == "+":
                st.append(st.pop() + st.pop())
            elif i == "-":
                s,f=st.pop(),st.pop()
                st.append(f-s)
            elif i == "*":
                st.append(st.pop() * st.pop())
            elif i == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))
            else:
                st.append(int(i))
        return st[0]