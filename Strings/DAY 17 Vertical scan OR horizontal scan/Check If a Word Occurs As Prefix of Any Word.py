class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        wordIn=1 # as the counting of word is from 1
        i=0
        n=len(sentence)
        m=len(searchWord)
        while i<n:
            j=0
            start=i #initial storing of pointer
            while i<n and sentence[i]!=' ': # to check upto each word
                i+=1
            end =i #end pointer
            k=start# start pointer
            while k<end and j<m and sentence[k]==searchWord[j]:# to check for each ocuurence
                    k+=1
                    j+=1
            if j==m:
                return wordIn
            wordIn+=1 
            i+=1
        return -1
