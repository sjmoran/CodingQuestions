'''
Implementation of the Shunting-yard algorithm
'''


class Stack(object):
    '''
    Basic stack implementation with pop, push and peek operations
    '''

    def __init__(self):
        '''
        Initialise stack as simple array
        '''
        self.stack = []

    def push(self, value):
        '''
        Add element to top of stack
        '''
        self.stack.append(value)

    def pop(self):
        '''
        Remove the topmost element
        '''
        value = None
        if len(self.stack) > 0:
            value = self.stack[len(self.stack) - 1]
            del self.stack[len(self.stack) - 1]
        return value

    def peek(self):
        '''
        Show the topmost element but do not remove
        '''
        value = None
        if len(self.stack) > 0:
            value = self.stack[len(self.stack) - 1]
        return value

    def print_stack(self):

        print "***"
        i = len(self.stack) - 1
        while i >= 0:
            print self.stack[i]
            i = i - 1
        print "***"


class Calculator(object):
    '''
    Calculator class that takes in an expression string and returns the evaluation of that expression
    '''

    def __init__(self, data):

        self.precedence_dict = {"+": 1, "-": 1,
                                "(": 2, ")": 2, "*": 3, "/": 3, "^": 4}
        self.data = data

    def precedence(self, char1, char2):

        if char1 is None:
            return False
        if char2 is None:
            return False

        level1 = self.precedence_dict[char1]
        level2 = self.precedence_dict[char2]

        if level1 > level2:
            return True

        return False

    def evaluate(self, operand1, operand2, operator):

        if "+" in operator:
            return int(operand1) + int(operand2)
        if "-" in operator:
            return int(operand1) - int(operand2)
        if "*" in operator:
            return int(operand1) * int(operand2)
        if "/" in operator:
            return int(operand1) / int(operand2)
        if "^" in operator:
            return int(operand1) ** int(operand2)

    def compute(self):
        '''
        Evaluates the given expression using operator and operand stacks
        '''
        operator_stack = Stack()
        operand_stack = Stack()

        for char in self.data:
            if char.isdigit():
                operand_stack.push(char)
            elif "(" in char:
                operator_stack.push(char)
            elif ")" in char:
                while operator_stack.peek() != "(":
                    operator = operator_stack.pop()
                    operand1 = operand_stack.pop()
                    operand2 = operand_stack.pop()
                    value = self.evaluate(operand2, operand1, operator)
                    operand_stack.push(value)
                operator_stack.pop()
            else:
                while self.precedence(char, operator_stack.peek()):
                    operator = operator_stack.pop()
                    operand1 = operand_stack.pop()
                    operand2 = operand_stack.pop()
                    value = self.evaluate(operand2, operand1, operator)
                    operand_stack.push(value)

                operator_stack.push(char)

        while operator_stack.peek() is not None:

            operator = operator_stack.pop()
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()
            operand_stack.push(self.evaluate(operand2, operand1, operator))

        return operand_stack.peek()

if __name__ == "__main__":

    calc = Calculator("2^5")
    print calc.compute()
