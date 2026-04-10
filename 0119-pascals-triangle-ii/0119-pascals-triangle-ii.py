class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rs=[]
        for i in range(rowIndex+1):
            ls = [1]*(i+1)
            for j in range(1,i):
                ls[j]=rs[i-1][j-1]+rs[i-1][j]
            rs.append(ls)
        return rs[rowIndex]
        