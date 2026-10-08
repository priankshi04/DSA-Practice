class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # when left pointer is not equal then we jump pointers to inner char
                a = left + 1
                b = right
                c = left
                d = right - 1
                # checks if the string is palindrome by skipping the left char
                while a < b and s[a] == s[b]:
                    a += 1
                    b -= 1
                # checks if the string is palindrome by skipping the right char
                while c < d and s[c] == s[d]:
                    c += 1
                    d -= 1
                return a >= b or c >= d
            left += 1
            right -= 1
        return True


