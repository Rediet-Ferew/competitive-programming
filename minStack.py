class MinStack:

    def __init__(self):
        self.elements = []
    def push(self, val: int) -> None:
        self.elements.append(val)

    def pop(self) -> None:
        if len(self.elements):
            self.elements.pop()
    def top(self) -> int:
        if len(self.elements):
            return self.elements[-1]
        
    def getMin(self) -> int:
        self.elements = sorted(self.elements)
        return self.elements[0]
        
         

