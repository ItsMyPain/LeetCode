class MinStack:
    data: list
    mn: list

    def __init__(self):
        self.data = []
        self.mn = []

    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.mn.append(val)
        if self.mn[-1] >= val:
            self.mn.append(val)
        self.data.append(val)

    def pop(self) -> None:
        if self.data[-1] == self.mn[-1]:
            self.mn.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mn[-1]


obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
