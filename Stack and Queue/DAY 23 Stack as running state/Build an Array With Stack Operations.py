class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        idx = 0

        for num in range(1, n + 1):
            ans+=["Push"]

            if num == target[idx]:
                idx += 1
            else:
                ans+=["Pop"]

            if idx == len(target):
                break

        return ans