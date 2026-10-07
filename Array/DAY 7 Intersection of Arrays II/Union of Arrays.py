class Solution:
    def findUnion(self, a, b):
        # code here
        c = a + b
        answer = []
        #Same as intersection of Arrays except I have first combined both the lists
        for i in c:
            found = False
            for j in answer:
                if i == j:
                    found = True
                    break
            if found == False:
                answer.append(i)
        return answer

