# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversedList(head):
    """
    :param head: a Node instance
    pre: previous node
    cur: current node
    suc: succeeding node
    :return: a reversed linked list
    """
    pre = None
    cur = head
    suc = None


    while cur:
        suc = cur.next
        cur.next = pre
        pre = cur
        cur = suc

    head = pre
    return head
