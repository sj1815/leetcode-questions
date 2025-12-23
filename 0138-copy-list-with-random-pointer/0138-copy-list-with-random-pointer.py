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
        if not head: return None

        curr = head
        map_node = {}

        while curr:
            node = Node(x=curr.val)
            map_node[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            new_node = map_node[curr]
            
            if curr.next:
                new_node.next = map_node[curr.next]
            else:
                new_node.next = None

            if curr.random:
                new_node.random = map_node[curr.random]
            else:
                new_node.random = None
            
            curr = curr.next

        return map_node[head]


        