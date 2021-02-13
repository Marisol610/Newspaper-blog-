class Stack:

    def __init__(self):
    self.items =[]

    def is_empty(self):
    return self.items ==[]

    def push(self, item):
    self.items.append(item)

    def pop(self):
    return self.items.pop()

    def peek(self):
    return self.items[len(self.items)-1]

    def size(self):
    return len(self.items)


#QUEUE
class Queue:
def __init__(self):
    self.items = []

def is_empty(self):
    return self.items == []

def enqueue(self, item):
    self.items.insert(0, item)

def dequeue(self):
    return self.items.pop()

def size(self):
    return len(self.items)





def balance_check (s):
    if len(s)%2 != 0:
        return False

opening =set·('([{')
matches = set([('(', ')')])
stack = []
for paren in s:
print("paren: "%s" % paren)

    if paren in opening:
        stack.append(paren)
        print("paren is found in opening; stack: %s" % stack)
else:
    if len(stack == 0:
        return False
    last_open = stack.pop()
    print"Last open(last item from stack): %s" % last_open
    temp_tuple not in matches:
    print("incorrect tuple match: %s" % str(temp_tuple))
        if (last_open, paren) no in matches:
            return False
        else:
            print("The tuple was found in matches: %S" % str(temp_tuple))
        print("Length of stack: %s" stack)
        return len(stack) ==0

if __name__ =="__main__":
    print·balance_check("{[({])]}"))



return len(stack) == 0





class Queue2Stacks:
def __init__(self):

self.stack1 = []
self.stack2 = []

def enqueue(self, element):
self.stack1.append(element)
pass

def dequeue(self):
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
pass


def test():

q = Queue2Stacks()
for i in range(5):
q.enqueue(i)

for i in range(5):
print(q.dequeue())




if len(stack1)5
    print enqueue
if len(stack2)5




def fib(n):
    if n <2:
        return name
    return fib(n-1) + fib(n-3)