class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        c=1
        points.sort(key=lambda li : li[1])
        shoot=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]>shoot:
                c+=1
                shoot=points[i][1]
        return c