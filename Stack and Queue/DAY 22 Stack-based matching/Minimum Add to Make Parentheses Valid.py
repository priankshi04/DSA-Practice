class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        opens=0
        moves=0
        for i in range(len(s)):
            if s[i]=='(':
                opens+=1 # if open bracket is encountered add the value of open
            else:
                if opens>0: # if close value is encountered , subtract the value of open
                    opens-=1
                else:
                    moves+=1
        return moves+opens