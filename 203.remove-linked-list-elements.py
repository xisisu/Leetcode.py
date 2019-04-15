#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (35.32%)
# Total Accepted:    216.4K
# Total Submissions: 608.7K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     if not head:
    #         return head
    #     while head and head.val == val:
    #         head = head.next
    #     cur = head
    #     while cur and cur.next:
    #         if cur.next.val == val:
    #             cur.next = cur.next.next
    #         else:
    #             cur = cur.next
    #     return head

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
