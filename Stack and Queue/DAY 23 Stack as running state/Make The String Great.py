class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [""] * len(s) # TO prepare the stack
        size = 0

        for ch in s: # for each char
            if size > 0 and abs(ord(ch) - ord(stack[size - 1])) == 32: #the current char and prevous char equals 32 , if yes , then the current char is not added and even the previous element is removed
                size -= 1
            else:
                stack[size] = ch # otherwise add the char
                size += 1

        answer = ""

        for i in range(size):
            answer += stack[i]

        return answer