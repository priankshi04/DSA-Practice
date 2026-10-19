class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        word = list(word)  # to convert the string to list
        j = 0
        while j < len(word):  # to travaerse each element
            if word[j] == ch:  # to get the element from where we have to reverse
                break
            j += 1  # to create the last pointer
        i = 0  # starting pointer
        if j < len(
                word):  # to check if the pointer is less than the length of the word otherwise the char does not exist and the reversing is kipped
            while i < j:  # to reverse the string
                temp = word[i]
                word[i] = word[j]
                word[j] = temp
                i += 1
                j -= 1

        result = ''  # to return the string
        for c in word:
            result += c
        return result
