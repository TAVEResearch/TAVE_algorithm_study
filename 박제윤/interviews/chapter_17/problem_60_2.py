# page: p502
# sol.2) insertion sort -> improve comparing condition 
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
  # init
  cur = parent = ListNode(0)

  while head:
    while cur.next and cur.next.val < head.val:
      cur = cur.next

    cur.next, head.next, head = head, cur.next, head.next

    # turn back when only necessary 
    if head and cur.val > int(head.val):
      cur = parent

  return parent.next

init_list()
print("not sorted")
print_list()
print("sorted")
insertionSortList(node_A)
print_list()
