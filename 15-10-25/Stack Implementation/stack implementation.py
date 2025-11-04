class Stack :
    def __init__(self):
        self.stack = []     # stack created using array
    
    def is_empty(self) :
        return len(self.stack) == 0
            
    
    def peek(self) :
        if self.is_empty() :
            print("stack is empty")
            return None
        else :
            res = self.stack[-1]
            print(self.stack[-1])
            return  res
            
        
    
    def push(self, num) :
        self.stack.append(num)
    
    def pop(self) :
        if self.is_empty() :
            return ("stack is already empty")
            return None
        else :
            val = self.stack[-1]
            
            print(f"popped value = {val}")

check = Stack()
check.push(4)
check.push(3)
check.push(2)
check.push(1)
check.pop()
check.peek()

        