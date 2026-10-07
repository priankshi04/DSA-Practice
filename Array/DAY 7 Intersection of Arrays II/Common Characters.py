class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        answer = []
        count = [0] * 26
        for i in range(len(words[0])):
            index = ord(words[0][i]) - ord('a')
            count[index] += 1

        for i in range(1, len(words)):
            current = [0] * 26

            for j in range(len(words[i])):
                index = ord(words[i][j]) - ord('a')
                current[index] += 1

            for j in range(26):
                if current[j] < count[j]:
                    count[j] = current[j]

        for i in range(26):
            for j in range(count[i]):
                answer.append(chr(i + ord('a')))

        return answer