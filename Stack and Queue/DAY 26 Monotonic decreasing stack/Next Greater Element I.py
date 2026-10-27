class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        n= len(pushed)
        stack = [0]*n
        top=-1 # initial stack index empty
        j = 0

        for i in range(n):
            top+=1 # increasing the stack index
            stack[top] = pushed[i] # pushing element to stack

            while top>=0 and j<n and stack[top]==popped[j]:
                top-=1
                j += 1

        return top == -1
