class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hashmap1={}
        hashmap2={}
        for i in s1:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        slow=0
        for j in range(len(s2)):
            if s2[j] in hashmap2:
                hashmap2[s2[j]]+=1
            else:
                hashmap2[s2[j]]=1
            if j-slow+1>len(s1):
                hashmap2[s2[slow]]-=1
                if hashmap2[s2[slow]]==0:
                    del hashmap2[s2[slow]]
                slow+=1
            if hashmap1==hashmap2:
                return True
        return False
