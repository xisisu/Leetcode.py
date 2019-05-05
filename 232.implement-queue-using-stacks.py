#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_ = []
        self.out_ = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.out_.pop(-1)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.out_) == 0:
            while len(self.in_) > 0:
                self.out_.append(self.in_.pop(-1))
        return self.out_[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.in_) == 0 and len(self.out_) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
