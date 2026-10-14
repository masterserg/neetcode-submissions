class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for i in operations:
            if i == '+':
                points.append(points[len(points)-1] + points[len(points)-2])
            elif i == 'C':
                points.pop()
            elif i == 'D':
                points.append(2*points[len(points)-1])
            else:
                points.append(int(i))
        return sum(points)