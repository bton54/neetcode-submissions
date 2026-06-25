# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we want to remove the node that is the length of the list - n

        # get the actual linked list mapped isnide of the nodes list

        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - n


        # if we're supposed to remove the start, just return the list without the head
        if removeIndex == 0:
            return head.next

        # simply adjust the pointer of the node at the index before we want to remove 
        # point it to the node after the index we want to remove
        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head



