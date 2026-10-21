class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer=""
        for i in s:
            if 'A'<=i<='Z':
                answer+=chr(ord(i)+32) # to first get the ascii value of uppercase and add 32 and then convert to character
            else:
                answer+=i
        return answer