class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #here we first check if the palindrome is even length or odd
        count = 0
        for i in range(len(s)):
            left=i
            right=i
            #it checks for the occurence of the string in odd length
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            left =i
            right=i+1
            # it checks for the occurence of the string in odd length
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count
