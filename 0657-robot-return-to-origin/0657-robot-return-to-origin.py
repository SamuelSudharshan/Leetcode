class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r=0
        l=0
        for i in moves:
            if i == 'U':
                r+=1
            if i == "D":
                r-=1
            if i == 'L':
                l+=1
            if i == 'R':
                l-=1
        return True if r == 0 and l == 0 else False

        