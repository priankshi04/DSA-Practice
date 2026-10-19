class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=list(s)
        start=0
        while start<len(s): # to create two pointers
            i=start
            j= min(start + k - 1, len(s) - 1) # to take the next pointer without excceding the length of the str
            while i<j: # to swap
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1
            start += 2 * k # to increment the pointer to move 2k space
        result='' # to return in form of string
        for ch in s:
            result+=ch
        return result