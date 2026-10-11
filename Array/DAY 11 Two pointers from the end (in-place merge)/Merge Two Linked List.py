'''  Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        class Solution:
            def sortedMerge(self, head1, head2):
                # code here
                if head1 is None:
                    return head2
                if head2 is None:
                    return head1
                if head1.data<= head2.data:
                    head= head1
                    head1 = head1.next
                else:
                    head = head2
                    head2 = head2.next

                current = head

                while head1 is not None and head2 is not None:
                    if head1.data <= head2.data:
                        current.next = head1
                        head1 = head1.next
                    else:
                        current.next = head2
                        head2 = head2.next

                    current = current.next

                if head1 is not None:
                    current.next = head1
                else:
                    current.next = head2
                return head