from collections import deque
class Stack:
    def __init__(self):
        self.stk = deque() #creating an empty deque and assigning it to self.stk

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        return self.stk.pop()

    def is_empty(self):
        return len(self.stk)==0

    def reverse_string(self,value):
        reverse_string = ""
        for char in value:
            self.push(char)
        while not self.is_empty():
            reverse_string= reverse_string+self.pop()

        return reverse_string



if __name__ == '__main__':
    s = Stack()
    input_string = input("Enter the string to be reversed: ")
    print("Reversed string is :", s.reverse_string(input_string))


