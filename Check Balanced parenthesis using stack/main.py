from collections import deque
class Stack:
    def __init__(self):
        self.stk = deque()

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        self.stk.pop()

    def is_empty(self):
        return len(self.stk)==0

    def is_balanced(self, item):
        matching_parenthesis ={')':'(', '}':'{',']':'['}
        for char in item:
            if char in '({[':
                self.push(char)

            elif char in ')}]':
                if self.is_empty() or self.pop()!=matching_parenthesis[char]:
                    return False

        return self.is_empty()



if __name__ == '__main__':
    s=Stack()
    print(s.is_balanced("))"))

