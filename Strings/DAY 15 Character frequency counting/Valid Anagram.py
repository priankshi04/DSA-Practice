class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1={}
        hashmap2={}
        for i in s:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for j in t:
            if j in hashmap2:
                hashmap2[j]+=1
            else:
                hashmap2[j]=1
        if hashmap1==hashmap2:
            return True
        else:
            return False
        
