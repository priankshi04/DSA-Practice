class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        moves = 0
        total = 0
        while total < target or (total - target) % 2 != 0:
            moves += 1
            total += moves
        return moves
