class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        h=[0]*n
        area=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    h[j]+=1
                else:
                    h[j]=0
            sh=sorted(h, reverse=True)
            for j in range(n):
                if sh[j]==0:
                    break
                area=max(area,sh[j]*(j+1))
        return area

        