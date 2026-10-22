class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[0]*len(s)
        top=-1
        for i in s:
            if i=='(' or i=='[' or i=='{': # if bracket opens append it to the stack
                top+=1
                stack[top]=i
            else: # if bracket close comes, check if the open is present or not using the top index
                if top==-1:
                    return False
                if i==')' and stack[top]=='(':
                    top-=1
                elif i==']' and stack[top]=='[':
                    top-=1
                elif i=='}' and stack[top]=='{':
                    top-=1
                else:
                    return False
        if top==-1:# if the stack is empty, then index of top would be -1
            return True
        else:
            return False
