class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool

        hashmap1={}
        hashmap2={}
        for i in word1:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for j in word2: # to take the frequency of char of both the words
            if j in hashmap2:
                hashmap2[j]+=1
            else:
                hashmap2[j]=1
        if hashmap1.keys() != hashmap2.keys():# to check if the word can be formed or not
            return False
        if sorted(hashmap1.values()) != sorted(hashmap2.values()):
            return False
        return True
        """
#Another approach 
        if len(word1) != len(word2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in word1:
            index = ord(ch) - ord('a')
            count1[index] += 1

        for ch in word2:
            index = ord(ch) - ord('a')
            count2[index] += 1

        for i in range(26):
            if count1[i] == 0 and count2[i] != 0:
                return False
            if count1[i] != 0 and count2[i] == 0:
                return False

        for i in range(26):
            for j in range(i + 1, 26):
                if count1[i] > count1[j]:
                    temp = count1[i]
                    count1[i] = count1[j]
                    count1[j] = temp

                if count2[i] > count2[j]:
                    temp = count2[i]
                    count2[i] = count2[j]
                    count2[j] = temp

        for i in range(26):
            if count1[i] != count2[i]:
                return False

        return True