class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val<= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.minstack[-1]==self.stack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack: return None
        return self.minstack[-1]
