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
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        size = 0
        while curr.next:
            size += 1
            curr = curr.next
        
        tar = (size // 2) + 1

        curr = dummy
        for i in range(tar):
            curr = curr.next
        
        return curr

        

        