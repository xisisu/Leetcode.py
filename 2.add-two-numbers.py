#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.00%)
# Likes:    5208
# Dislikes: 1339
# Total Accepted:    880.6K
# Total Submissions: 2.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     carry = 0
    #     dummy = ListNode(-1)
    #     cur = dummy
    #     while l1 or l2 or carry != 0:
    #         val = carry
    #         if l1:
    #             val += l1.val
    #             l1 = l1.next
    #         if l2:
    #             val += l2.val
    #             l2 = l2.next
    #         cur.next = ListNode(val % 10)
    #         cur = cur.next
    #         carry = val // 10
    #     return dummy.next            
            
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     lists = [l1, l2]
    #     carry = 0
    #     dummy = ListNode(-1)
    #     cur = dummy
    #     while lists or carry != 0:
    #         carry += sum(a.val for a in lists)
    #         lists = [a.next for a in lists if a.next]
    #         cur.next = ListNode(carry % 10)
    #         carry //= 10
    #         cur = cur.next
    #     return dummy.next       
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toInt(node: ListNode) -> int:
            return node.val + 10 * toInt(node.next) if node else 0
        def toList(n: int) -> ListNode:
            node = ListNode(n % 10)
            if n > 9:
                node.next = toList(n // 10)
            return node
        return toList(toInt(l1) + toInt(l2))


