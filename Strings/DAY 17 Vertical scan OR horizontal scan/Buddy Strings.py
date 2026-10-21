class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal): # to check if the goal length is present in the string
            return False
        diff=[]
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += [i]

        if len(diff) == 0:
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    if s[i] == s[j]:
                        return True
            return False

        if len(diff) != 2:
            return False

        i = diff[0]
        j = diff[1]

        return s[i] == goal[j] and s[j] == goal[i]