from abc import *

#AbstractExpression
class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context):
        pass

#TerminalExpression
class TerminalExpression(Expression):
    def __init__(self, data):
        self.__data = data

    def interpret(self, context):
        if self.__data in context:
            return True
        else:
            return False

#NonTerminalExpression
class OrExpression(Expression):
    def __init__(self, exp1, exp2):
        self.__exp1 = exp1
        self.__exp2 = exp2

    def interpret(self, context):
        return self.__exp1.interpret(context) or self.__exp2.interpret(context)

    # NonTerminalExpression
class AndExpression(Expression):
    def __init__(self, exp1, exp2):
        self.__exp1 = exp1
        self.__exp2 = exp2

    def interpret(self, context):
        return self.__exp1.interpret(context) and self.__exp2.interpret(context)


John = TerminalExpression("John")
Mary = TerminalExpression("Mary")
married = TerminalExpression("Married")
single = TerminalExpression("Single")

isMarried = AndExpression(John, married)
isSingle = AndExpression(Mary, single)
context = input()
print(isMarried.interpret(context))
context = input()
print(isSingle.interpret(context))