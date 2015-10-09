__author__ = 'weiqi'

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxa = 0
        length = len(points)
        if length <= 1:
            return length
        for si in range(0,length):
            maxv = 0
            dict1 = {}
            dup = 0
            sp = points[si]
            for ei in range(si+1, length):
                ep = points[ei]
                if(sp.y-ep.y)==0:
                    if(sp.x-ep.x)==0:
                        dup += 1
                    else:
                        dict1['x']=dict1.get('x',1) + 1
                else:
                    lean = float((sp.x-ep.x))/(sp.y-ep.y)
                    dict1[lean]=dict1.get(lean,1)+1
            values = dict1.values()
            for value in values:
                if value > maxv:
                    maxv = value
            maxv = max(1,maxv) + dup
            maxa = max(maxa,maxv)
        return maxa

from collections import namedtuple
Point = namedtuple('Point', 'x y')
testData = [Point(x=-4,y=-4),Point(x=-8,y=-582),Point(x=-3,y=3),Point(x=-9,y=-651),Point(x=9,y=591)]
sol = Solution()
print sol.maxPoints(testData)