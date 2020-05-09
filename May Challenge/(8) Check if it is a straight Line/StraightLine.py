'''
Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

 Hide Hint #1
If there're only 2 points, return true.

Hide Hint #2
Check if all other points lie on the line defined by the first 2 points.

Hide Hint #3
Use cross product to check collinearity..
'''
def slope(x, y):
    if ((x[0] - y[0]) == 0  or (x[1]-y[1]) == 0):
        return 0
    return float((x[0] - y[0]) / (x[1] - y[1]))

class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        x = coordinates[0]
        y = coordinates[1]
        sl1 = slope(x,y)
        for i in range(1,len(coordinates)):
            x = coordinates[0]
            y = coordinates[i]
            sl2 = slope(x,y)
            if (sl1 != sl2):
                return False
        return True

s= Solution()
print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
