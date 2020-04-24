
class MinMaxStack(object):
    def __init__(self):
        self.stack = []
        self.min_max_stack = []
    
    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        min_max_child = {"min": number, "max": number}
        if len(self.min_max_stack):
            last_inserted_child = self.min_max_stack[len(self.min_max_stack) - 1]
            min_max_child["min"] = min(last_inserted_child["min"], min_max_child["min"])
            min_max_child["max"] = max(last_inserted_child["max"], min_max_child["max"])
        self.min_max_stack.append(min_max_child)
        self.stack.append(number)

    def getMin(self):
        top_min_max_stack = self.min_max_stack[len(self.min_max_stack) - 1]
        return top_min_max_stack["min"]

    def getMax(self):
        top_min_max_stack = self.min_max_stack[len(self.min_max_stack) - 1]
        return top_min_max_stack["max"]
    
    def printStack(self):
        print(20*"*")
        print(self.stack)
        print(self.min_max_stack)
        print(20*"*")

stack = MinMaxStack()
stack.push(2)
stack.push(3)
stack.push(1)
stack.push(11)
stack.push(7)

stack.printStack()

print(stack.getMin())
print(stack.getMax())