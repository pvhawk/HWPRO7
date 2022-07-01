from stack import Stack

def brackets_correctly(str):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    s = Stack()
    for i in str:
        if i in brackets_open:
            s.push(i)
        if i in brackets_closed:
            if s.size() == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if s.peek() == open_bracket:
                s.pop()
            else:
                return False
    if s.size() != 0:
        return False
    return True


if __name__ == '__main__':
    str = input("Enter string brackets:\n")

    if brackets_correctly(str) == True:
        print("Сбалансированно")
    else:
        print("Несбалансированно")
