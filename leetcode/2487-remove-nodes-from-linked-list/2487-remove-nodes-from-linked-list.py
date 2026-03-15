# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #reversal to apply increasing order from the back
        prev = None
        curr = head       
        while curr:
            temp = curr.next
            curr.next= prev
            prev = curr
            curr = temp
        #removal of non_increaing order
        curr= prev
        max_val = prev.val
        while curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                max_val = curr.next.val
                curr = curr.next
        #reversing again to get the original order
        new_prev = None
        new_curr = prev 
        while new_curr:
            temp = new_curr.next    
            new_curr.next = new_prev 
            new_prev = new_curr     
            new_curr = temp     
            
        return new_prev



        

        