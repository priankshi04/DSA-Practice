class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap={}
        ans=""
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1 # prepared the dict
        while hashmap:
            maxCh="" # to keep the element which has max freq
            maxF=0
            for i in hashmap:
                if hashmap[i]>maxF:
                    maxF=hashmap[i]#to take the value of the freq
                    maxCh=i# to take the element
            ans+=maxCh*maxF # to return the string by making it using the element and its freq
            del hashmap[maxCh] # to del that char after adding to the srtring
        return ans