class Stack:
    def __init__(self):
        self.stack = []
        self.max = -1
    def push(self,x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.max = x
        else:
            if x <= self.max:
                self.stack.append(x)
            else:
                self.stack.append(2 * x - self.max)
                self.max = x
    def pop(self):
        assert(len(self.stack))
        y = self.stack.pop()
        if y > self.max:
            self.max = 2 * self.max - y
    def get_max(self):
        assert(len(self.stack))
        return self.max
    def get_len(self):
        return len([i for i in self.stack])
    def __repr__(self):
        return ' '.join([str(i) for i in self.stack]) 
