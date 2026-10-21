class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=len(s)-1
        count=0
        while i>=0 and s[i]==' ': # to remove space from the last word
            i-=1
        while i>=0 and s[i]!=' ': # to count the letter in the last word before whitespace occurs
            count+=1
            i-=1
        return count