class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # empty list
        answer = []
        used = []
        # creating a list where the elements is based on the length of whose element are searched with j
        for i in range(len(nums2)):
            used.append(False)

        for i in range(len(nums1)):
            for j in range(len(nums2)):

                if nums1[i] == nums2[j] and used[j] == False:
                    answer.append(nums1[i])
                    used[j] = True
                    break

        return answer
