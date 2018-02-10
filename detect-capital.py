class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        D= 0
        d= 0
        w= list( word )
        for i in w:
            if i <= "Z":
                D+= 1
            if i >= "a":
                d+= 1
        print(D)
        print(d)
        return ( D == len(word) or ( d == len(word)) or ( D == 1 and w[0] <= "Z" ))
    