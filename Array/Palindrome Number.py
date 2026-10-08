class Solution:
    def isPalindrome(self, n):
            # code here
            # to remove the negative sign
        n=abs(n)
        original= n
        reverse = 0
        # to get the last digit and multiply with 10 to get the reverse of the number
        while n>0:
            digit= n%10
            reverse= reverse*10 + digit
            n=n//10
        if original== reverse:
                return True
        else:
                return False