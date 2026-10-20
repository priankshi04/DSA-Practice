class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap={}
        for word in strs:
            count=[0]*26 #for 26 aplhabets
            for ch in word:
                index=ord(ch)-ord('a')
                count[index]+=1
            key = tuple(count)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]
        answer=[]
        for group in hashmap.values():
            answer.append(group)
        return answer