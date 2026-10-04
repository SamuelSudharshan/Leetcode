class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[0] * len(temperatures)
        st=[]
        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                prev=st.pop()
                ans[prev] = i - prev
            st.append(i)
        return ans