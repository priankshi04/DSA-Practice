class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        answer = []
        for word in words:
            hashmap1 = {}
            hashmap2 = {}
            match = True
            for i in range(len(pattern)):
                ch1 = pattern[i]  # to get the first char in string s
                ch2 = word[i]  # to get the first char in string t
                if ch1 in hashmap1:
                    if hashmap1[ch1] != ch2:  # mapping the element to another char of another str
                        match = False
                        break
                else:
                    hashmap1[ch1] = ch2  # if not present , map it

                if ch2 in hashmap2:  # to check the same
                    if hashmap2[ch2] != ch1:
                        match = False
                        break
                else:
                    hashmap2[ch2] = ch1

            if match:
                answer.append(word)
        return answer
