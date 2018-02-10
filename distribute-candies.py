class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d= int( len( candies )/2 )
        c= len( set(candies) )
        return min( c, d )