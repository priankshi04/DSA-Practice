# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
     #BRUTE FORCE APPROACH
        visited = []

        current = head

        while current:
            for node in visited:
                if node == current:
                    return True

            visited.append(current)
            current = current.next
#TC: o(n^2)
#sc: o(n)
        return False
#OPTIMAL APPROACH
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
 #TC:O(N)
 #SC:O(1)
