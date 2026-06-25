"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # we should probably use an oldToNew map for deep copy liek in the graph
        # given the question style - we should know to use map old nodes to the new ones
        oldToNew = {None: None}
        cur = head

        while cur: # while this current node still exists
            # let's make a copy of it and then push the current to the next
            # we are building out just the nodes

            copy = Node(cur.val)
            oldToNew[cur] = copy # we map the old node to the copy

            cur = cur.next
        # reset the current pointer to the ehad after adjusting it here
        cur = head
        while cur:
            # now we want to retrieve the copies and set up the pointers (next, rand)
            # see what node this cur maps to
            copy = oldToNew[cur]
            # set the copy's next to the copy that the original cur's next maps to
            copy.next = oldToNew[cur.next]

            # do the same with the random pointer
            copy.random = oldToNew[cur.random]
            
            # go fwd - do this for the rest
            cur = cur.next

        return oldToNew[head]



            

