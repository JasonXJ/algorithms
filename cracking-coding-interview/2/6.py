class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def find_circle_head(head):
    seen_nodes = set()
    while head is not None:
        if head in seen_nodes:
            return head
        seen_nodes.add(head)
        head = head.next

if __name__ == '__main__':
    node_a = Node('A', Node('B', Node('C', Node('D', Node('E')))))
    node_c = node_a.next.next
    node_e = node_c.next.next
    node_e.next = node_c
    print(find_circle_head(node_a).data)
