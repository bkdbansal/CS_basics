"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


"""


# Time:  O(n)
# Space: O(1)
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#


### Stack : 「Last-In-First-Out」
### http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html

 
# V1  : dev 
"""

class MinStack(object):

    def __init__(self):
        self.min = None
        self.stack = []
        

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        return self.stack.pop()


    def top(self):
        return self.stack[0]
        

    def getMin(self):
        return min(self.stack)
        
"""


# V2 
# https://www.cnblogs.com/zuoyuan/p/4091870.html
# stack1 : regular stack
# stack2 : stack for return minimum in-stack element 

class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    # @return an integer
    def push(self, x):
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    # @return nothing
    def pop(self):
        top = self.stack1[-1]
        self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()
        
    # @return an integer
    def top(self):
        return self.stack1[-1]

    # @return an integer
    def getMin(self):
        return self.stack2[-1]




# V3 
class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    # @return an integer
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    # @return an integer
    def getMin(self):
        return self.min

# Time:  O(n)
# Space: O(n)
class MinStack2:
    def __init__(self):
        self.stack, self.minStack = [], []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack):
            if x < self.minStack[-1][0]:
                self.minStack.append([x, 1])
            elif x == self.minStack[-1][0]:
                self.minStack[-1][1] += 1
        else:
            self.minStack.append([x, 1])

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1][0]

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-1)
    print [stack.top(), stack.getMin()]