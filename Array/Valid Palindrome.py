class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Using pointer left and right to check the palindrome
        left = 0
        right = (len(s) - 1)
        while left < right:
            # If s[left] is not alphanum char , then pass it by incrementing
            if not (('a' <= s[left].lower() <= 'z') or ('0' <= s[left] <= '9')):
                left += 1
            # similar with starting at last pointer
            elif not (('a' <= s[right].lower() <= 'z') or ('0' <= s[right] <= '9')):
                right -= 1
            # now if both it checks only for alphabets from left and right
            else:
                if s[left].lower() != s[right].lower():
                    return False

                left += 1
                right -= 1
        return True
