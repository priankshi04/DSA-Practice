class Solution(object):
    def reverseString(self, s):
        def reverse(i, j):

            if i >= j:#base 
                return

            s[i], s[j] = s[j], s[i] #swapping 
            reverse(i + 1, j - 1) #recursive

        reverse(0, len(s) - 1)
        return s
