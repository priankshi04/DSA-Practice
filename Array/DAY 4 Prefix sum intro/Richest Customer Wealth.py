class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        p=[] # empty list
        for i in range(0,len(accounts)):#to access the lsit element
            ans=0
            for j in range(0,len(accounts[i])):# to access inside each i element
                ans+=accounts[i][j] # to perform prefix sum
            p+=[ans] # adding the element to a new list
        r=p[0] # assigning first value of list p to k
        for k in range(0,len(p)): # to take the length of p
            if p[k]>r:
                r=p[k] # find the max value
        return r
