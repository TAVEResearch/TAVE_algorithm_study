# page: p494
# sol.3) Built-in function & from Linked list to List
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
def sortList(head: ListNode) -> ListNode:
  # Linked list -> List
  p = head
  lst: List = []

  while p:
    lst.append(p.val)
    p = p.next

  # sorting
  lst.sort()

  # List -> Linked list
  p = head
  for i in range(len(lst)):
    p.val = lst[i]
    p = p.next

  return head
  
init_list()
print("not sorted")
print_list()
sortList(node_A)
print("sorted")
print_list()
