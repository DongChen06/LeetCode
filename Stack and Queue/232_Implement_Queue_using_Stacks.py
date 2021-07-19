class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        if len(self.stack2) != 0:
            temp = self.stack2[-1]
            self.stack1 = self.stack2[:-1][::-1]
            self.stack2 = []
            return temp
        else:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        if len(self.stack2) != 0:
            temp = self.stack2[-1]
            self.stack1 = self.stack2[::-1]
            self.stack2 = []
            return temp
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
obj.push(5)
param_3 = obj.peek()
param_4 = obj.pop()
param_5 = obj.pop()
param_6 = obj.pop()
param_7 = obj.pop()
param_8 = obj.empty()