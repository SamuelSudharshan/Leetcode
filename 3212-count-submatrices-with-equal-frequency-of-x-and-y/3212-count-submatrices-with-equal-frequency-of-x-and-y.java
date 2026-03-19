class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int[] sumx = new int[cols];
        int[] sumy = new int[cols];
        int res=0;
        for (int i = 0; i<rows;i++){
            int rx=0,ry=0;
            for(int j=0;j<cols;j++){
                if (grid[i][j]=='X') rx++;
                else if (grid[i][j]=='Y')ry++;
                sumx[j]+=rx;
                sumy[j]+=ry;
                if (sumx[j]>0 && sumx[j]==sumy[j]) res++;
            }
            
        }
        return res;
    }
}