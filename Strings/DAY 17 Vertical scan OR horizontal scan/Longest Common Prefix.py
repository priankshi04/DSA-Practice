class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        for i in range(len(strs[0])):# to take the first word
            ch=strs[0][i]# to take the first char of the word
            for j in range (1,len(strs)): # to compare with other words
                if i>=len(strs[j]) or strs[j][i]!=ch: # to check if the i length is greater than the new str or if the char matches
                    return ans
            ans+=ch # if it matches appending
        return ans
