class MinStack:

    def __init__(self):
        self.small = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.small:
            self.small.append(val)
        else:
            self.small.append(min(self.small[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.small = self.small[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.small[-1]