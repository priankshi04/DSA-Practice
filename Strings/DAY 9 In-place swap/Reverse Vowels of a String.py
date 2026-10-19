
class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        i = 0
        j = len(s) - 1
        vowels = 'aeiouAEIOU'

        while i < j: # to check if ti is a vowel or not , if not increment value
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels: # same decrement value
                j -= 1
            else:
                s[i],s[j]=s[j],s[i] #to swap the char
                i += 1
                j -= 1

        result = "" # to return the string
        for ch in s:
            result += ch

        return result
