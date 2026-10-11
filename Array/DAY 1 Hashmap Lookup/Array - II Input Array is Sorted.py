class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # taking two pointers
        fast =0
        slow= len(numbers)-1
        while fast< slow:
            #checking if the sum of numbers is equal to target or not
            if numbers[fast]+ numbers[slow]== target:
                return fast+1, slow+1 # if yes give the index in counting terms
            elif numbers[fast]+numbers[slow]> target:
                slow-=1 #as sum is greater and the array is sorted so we need to
            else:
                fast+=1
