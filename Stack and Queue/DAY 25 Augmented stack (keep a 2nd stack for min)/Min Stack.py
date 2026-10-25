class MinStack(object):

    def __init__(self):
        self.stack=[0]*30000
        self.min_stack=[0]*30000
        self.top_index=-1
        self.min_index=-1   

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.top_index+=1
        self.stack[self.top_index]=value
        if self.min_index == -1 or value <= self.min_stack[self.min_index]:
            self.min_index+=1
            self.min_stack[self.min_index]=value
        

    def pop(self):
        """
        :rtype: None
        """
        val=self.stack[self.top_index]
        self.top_index-=1
        if val == self.min_stack[self.min_index]:
            self.min_index-=1
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.top_index]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[self.min_index]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
