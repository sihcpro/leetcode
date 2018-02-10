class Solution:
    def removeElement(self, n, m):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if n == []:
            return 0
        i= d= 0
        j= l= len(n)-1

        while i <= j and i <= l and j >= 0:
            while i <= l and n[i] != m:
                i+= 1
            while j >= 0 and n[j] == m:
                j-= 1
            if i < j:
                n[i], n[j]= n[j], n[i]
            i+= 1
            j-= 1
                
        
        return l-n.count(m)+1
        