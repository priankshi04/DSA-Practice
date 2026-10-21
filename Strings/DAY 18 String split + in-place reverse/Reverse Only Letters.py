class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        left = 0
        right = len(s)-1
        #here check where is the special character is present where we have to reverse it
        while left<right:
            if not (('a'<=s[left]<='z')or ('A'<=s[left]<='Z')):
                left+=1
            elif not (('a'<=s[right]<='z')or ('A'<=s[right]<='Z')):
                right-=1
            else:
        # classic method to swap the first and the last element in the list
                temp=s[left]
                s[left]=s[right]
                s[right]=temp
                left+=1
                right-=1
        # again converting the list into string
        answer=''
        for i in range(len(s)):
            answer+=s[i]
        return answer