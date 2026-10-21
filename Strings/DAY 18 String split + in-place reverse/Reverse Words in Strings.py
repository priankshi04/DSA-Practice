class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer=''
        i=len(s)-1
        while i>=0:
            while i>=0 and s[i]==' ': # to ignore whitespaces
                i-=1

            if i<0:
                break
            j=i

            while i>=0 and s[i]!=' ': # to get each word and until whitespace is encountered
                i-=1
            if answer != "":
                answer+=' '
            answer+=s[i+1:j+1]
        return answer