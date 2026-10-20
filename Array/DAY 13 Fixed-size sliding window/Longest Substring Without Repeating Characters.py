class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow = 0  # pointer
        maxLen = 0
        seen = []  # empty list
        for fast in range(0, len(s)):  # to take the range as the length of the string
            while s[fast] in seen:  # to move the window by removing the firat element and introducing the indented one
                seen.remove(s[slow])
                slow += 1
            seen.append(s[fast])

            length = fast - slow + 1  # to get the length of the substring b takeing the index of  first element and last element and including both of them
            if length > maxLen:
                maxLen = length
        return maxLen
