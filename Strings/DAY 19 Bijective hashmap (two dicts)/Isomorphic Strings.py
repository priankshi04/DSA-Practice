class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1 = {}
        hashmap2 = {}

        for index in range(len(s)):
            i=s[index] # to get the first char in string s
            j=t[index] # to get the first char in string t
            if i in hashmap1:
                if hashmap1[i] != j: # mapping the element to another char of another str
                    return False
            else:
                hashmap1[i] = j # if not present , map it

            if j in hashmap2: # to check the same
                if hashmap2[j] != i:
                    return False
            else:
                hashmap2[j] = i

        return True
