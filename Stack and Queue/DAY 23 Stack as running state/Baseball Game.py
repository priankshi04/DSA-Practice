class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record=[0]*len(operations) # to create a list with length of the records
        size=0
        for op in operations: # to perform necessary op for given symbols
            if op=='C':
                size-=1
            elif op=='D':
                record[size]=record[size-1]*2
                size+=1
            elif op=='+':
                record[size]=record[size-1]+record[size-2]
                size+=1
            else:
                record[size]= int(op) #to create a integer of the list
                size+=1
        total=0
        for i in range(size):
            total+=record[i] # to get the total
        return total
        
