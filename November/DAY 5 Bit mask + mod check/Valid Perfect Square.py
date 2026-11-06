class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=1
        while i*i<=num:
            if i*i==num:
                return True
            i+=1
        return False
        TC:O(squareroot n)
        SC:O(1)

        # OPTIMAL APPROACH # using binary search
        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
        TC: O(log n)
        SC: O(1)

