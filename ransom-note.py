class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote= sorted(list(ransomNote))
        magazine= sorted(list(magazine))
        i= 0
        for j in ransomNote:
            while i < len(magazine) and magazine[i] != j:
                i+= 1
            if i == len(magazine):
                return False
            i+= 1
        return True