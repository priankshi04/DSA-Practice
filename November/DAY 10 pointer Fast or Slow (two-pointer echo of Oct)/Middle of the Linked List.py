# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #optimal approach
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
        #TC:O(n)
        #SC:O(1)
        
        #Brute Force
        arr=[]
        curr=head
        while curr is not None:
            arr.append(curr)
            curr= curr.next
        mid=len(arr)//2
        return arr[mid]
        #TC:O(n)
        #SC:O(n)
        
