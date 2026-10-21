class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s= list(s)# to convert the string to list
        i=0
        for j in range(len(s)+1): # to travaerse each word
            if j==len(s) or s[j]== ' ':
                left=i # to create pointer for each word before whitespace
                right =j-1

                while left<right:# to reverse the string
                    temp=s[left]
                    s[left]=s[right]
                    s[right]=temp
                    left+=1
                    right-=1

                i=j+1 # to get to the next word
        result='' # to return the string
        for ch in s:
            result+= ch
        return result


