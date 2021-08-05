# page: p500
# sol.1) insertion sort
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def init_list() -> None:
  global node_A
  node_A = ListNode('4')
  node_B = ListNode('2')
  node_C = ListNode('1')
  node_D = ListNode('3')

  node_A.next = node_B
  node_B.next = node_C
  node_C.next = node_D

def print_list() -> None:
  global node_A
  node = node_A

  while node:
    print("node value: ", node.val)
    node = node.next
"""
################
my code is here
################
"""
def insertionSortList(head: ListNode) -> ListNode:
  cur = parent = ListNode(None)

  while head:
    while cur.next and cur.next.val < head.val:
      cur = cur.next

    cur.next, head.next, head = head, cur.next, head.next

    cur = parent

  return cur.next

init_list()
print("not sorted")
print_list()
print("sorted")
insertionSortList(node_A)
print_list()
