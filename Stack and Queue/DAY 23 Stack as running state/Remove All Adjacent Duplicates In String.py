class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =['']*len(s)
        size=0
        for ch in s:
            if size>0 and ch == stack[size-1]:
                size-=1
            else:
                stack[size]=ch
                size+=1
        answer=''
        for i in range(size):
            answer+=stack[i]
        return answer 