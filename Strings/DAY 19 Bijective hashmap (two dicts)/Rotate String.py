class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal): # to check if the goal length is present in the string
            return False
        combine= s+s # to add str twice so that the combination would result in any goal if roation occurs from any char
        if goal in combine:
            return True
        return False
        # using hashmap approach
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            rotated = s[i:] + s[:i]

            if rotated == goal:
                return True

        return False
