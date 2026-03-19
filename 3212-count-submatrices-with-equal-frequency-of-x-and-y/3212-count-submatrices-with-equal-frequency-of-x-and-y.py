class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        sumx=[0]*n
        sumy=[0]*n
        res=0
        for i in range(m):
            rx=0
            ry=0
            for j in range(n):
                if grid[i][j] == 'X':
                    rx += 1
                elif grid[i][j] == 'Y':
                    ry+=1
                sumx[j]+=rx
                sumy[j]+=ry
                if sumx[j]>0 and sumx[j] == sumy[j]:
                    res+=1
        return res
                    

        