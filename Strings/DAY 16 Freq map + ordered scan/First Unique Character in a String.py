class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hashmap={} # empty dict
        for i in s:# to traverse each char
            if i in hashmap: # to increase the frequency if present
                hashmap[i]+=1
            else: # to add the char in the dict
                hashmap[i]=1
        for i in range(len(s)): # to traverse each element in the str 
            if hashmap[s[i]]==1: #to check first unique element that has the frequency one while comparing with the str
                return i
        return -1
                


        
