class Solution(object):
    def intersection(self, nums1, nums2):
        answer=[]
#same approach but need to remove repeating appearing values
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]== nums2[j]:
                    already = False

                    for k in range(len(answer)):
                        if answer[k]==nums1[i]:
                            already = True
                            break
                    if already == False:
                        answer.append(nums1[i])
                    break
        return answer