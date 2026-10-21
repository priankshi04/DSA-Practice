class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap={}
        for i in s:
            if i in hashmap:# this checks if the char is already present , so it checks for 2nd occurenece ans as c is occured second index , so it return c
               return i
            else:
                hashmap[i]=1 # to create new key value 