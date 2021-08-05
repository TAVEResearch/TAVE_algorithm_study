# p500
# No.60
import ListNode

listnode = ListNode.ListNode


def insertionSort(head: listnode) -> listnode:
    cur = parent = listnode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        cur = parent
    return cur.next


def insertionSort_(head: listnode) -> listnode:
    cur = parent = listnode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next
        if head and cur.val > head.val:
            cur = parent
    return cur.next
