# p489
# No.58
import ListNode


def mergeTwolist(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = mergeTwolist(l1.next, l2)

    return l1 or l2


def sortList(head: ListNode) -> ListNode:
    if not (head and head.next):
        return head
    half, slow, fast = None, head, head
    while fast and fast.next:
        print(fast and fast.next)
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    l1 = sortList(head)
    l2 = sortList(slow)

    return mergeTwolist(l1, l2)


# EX: 내장 함수
def sortList_(head: ListNode) -> ListNode:
    p = head
    lst: list = []
    while p:
        lst.append(p.val)
        p = p.next

    lst.sort()

    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    return head


if __name__ == '__main__':
    a = ListNode.ListNode(3)
    b = ListNode.ListNode(1, a)
    c = ListNode.ListNode(2, b)
    d = ListNode.ListNode(4, c)
    linkedList = ListNode.linkedlist(d)
    sortList(linkedList.head)
    # TODO: 연결리스트 head 변경 할 수 있게 하기
    print(linkedList.head.val)
