class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashmap={}
        slow=0
        ans=0
        maxF=0
        for fast in range(len(s)):
            if s[fast] in hashmap:
                hashmap[s[fast]]+=1 # to create a dictionary
            else:
                hashmap[s[fast]]=1
            if hashmap[s[fast]]>maxF:
                maxF=hashmap[s[fast]] # to get the max frequency of char in the dict
            while (fast-slow+1)-maxF>k: # sliding window
                hashmap[s[slow]]-=1
                slow+=1
            if fast - slow + 1 > ans:
                ans = fast - slow + 1

        return ans