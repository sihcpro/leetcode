class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l= list( set(list1) & set(list2) )
        b= []
        for i in l:
            b.append( list1.index(i) + list2.index(i) )
        c= []
        for i, j in enumerate(l):
            if b[i] == min(b):
                c.append(j)
            # pass
        return c