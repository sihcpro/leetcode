class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w= 1
        l= area
        for i in range( 2, int(math.sqrt(area))+1):
            if area % i == 0:
                w= i
                l= int( area/i )
        return [l, w]
            