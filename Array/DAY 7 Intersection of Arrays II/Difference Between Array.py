class Solution:
    def findDifference(self, nums1, nums2):
        answer1 = []
        answer2 = []

        for i in range(len(nums1)):
            found = False

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                    break

            if found == False:
                already = False

                for k in range(len(answer1)):
                    if answer1[k] == nums1[i]:
                        already = True
                        break

                if already == False:
                    answer1.append(nums1[i])

        for i in range(len(nums2)):
            found = False

            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    found = True
                    break

            if found == False:
                already = False

                for k in range(len(answer2)):
                    if answer2[k] == nums2[i]:
                        already = True
                        break

                if already == False:
                    answer2.append(nums2[i])

        return [answer1, answer2]
