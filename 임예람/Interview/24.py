class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()

    def peek(self):
        #output이 없으면 모두 재입력
        if not self.output:
            while self.input: #input이 존재하지 않을 때까지
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []