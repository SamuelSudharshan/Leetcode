class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rs=[]
        for i in range(numRows):
            ls = [1] * (i+1)
            for j in range(1,i):
                ls[j]=rs[i-1][j-1] + rs[i-1][j]
            rs.append(ls)
        return rs
            
