class MyStack:
    
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.size != 0:
            return self.stack.pop()

    def size(self):
        return len(self.stack)


def balance(expression):
    open_list = ['[', '{', '(']
    close_list = [']', '}', ')']
    stack = MyStack()
    for charecter in expression:
        if charecter in open_list:
            stack.push(charecter)
        elif charecter in close_list:
            position = close_list.index(charecter)
            if (stack.size() != 0) and (stack.pop() != open_list[position]):
                return False
    return True

if __name__ == '__main__':
    exp = input("Enter experession :")
    isBalanced = balance(str(exp))
    print(isBalanced)
    