class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hashmap1 = {}
        hashmap2 = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):  # same as isomorphic just need to pair with the word
            ch = pattern[i]
            word = words[i]
            if ch in hashmap1:
                if hashmap1[ch] != word:
                    return False
            else:
                hashmap1[ch] = word
            if word in hashmap2:
                if hashmap2[word] != ch:
                    return False
            else:
                hashmap2[word] = ch
        return True


