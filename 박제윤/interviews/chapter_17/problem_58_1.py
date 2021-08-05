# page: p489
# sol.1) Merge sort using Runner
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def init_list() -> None:
  global node_A
  node_A = ListNode('-1')
  node_B = ListNode('5')
  node_C = ListNode('3')
  node_D = ListNode('4')
  node_E = ListNode('0')

  node_A.next = node_B
  node_B.next = node_C
  node_C.next = node_D
  node_D.next = node_E
  
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
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
  if l1 and l2:
    if l1.val > l2.val:
      l1, l2 = l2, l1
    l1.next = mergeTwoLists(l1.next, l2)

  return l1 or l2

def sortList(head: ListNode) -> ListNode:
  if not (head and head.next):
    return head
  
  # Runner
  half, slow, fast = None, head, head

  while fast and fast.next:
    half, slow, fast = slow, slow.next, fast.next.next
  half.next = None

  # divided recursive call
  l1 = sortList(head)
  l2 = sortList(slow)

  return mergeTwoLists(l1, l2)

init_list()
print("not sorted")
print_list()
sortList(node_A)
print("sorted")
print_list()
