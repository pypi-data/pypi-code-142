from fractions import Fraction
import abc

# Create your views here.
class AlgebraFactory:

    @abc.abstractmethod
    def solve():
        pass
    
    #Import from CoefficientFactory and EvaluateFactory

class CoefficientFactory:
    
    @abc.abstractmethod
    def add():
        pass

    @abc.abstractmethod
    def subtract():
        pass

    @abc.abstractmethod
    def multiply():
        pass

    @abc.abstractmethod
    def divide():
        pass

class EvaluateFactory:
    
    @abc.abstractmethod
    def evaluateExpression():
        pass

    @abc.abstractmethod
    def processAnOperator():
        pass

class EvaluateLinearEquations(EvaluateFactory): 

    def __init__(self,iexpression, iunknownChars):
        self.expressions = str(iexpression)
        self.unknownChars = iunknownChars
        self.operatorStack = list()
        self.operandStack = list()
        self.tokens = list()
    
    def isUnknown(self, c):
        if c in self.unknownChars:
            return True
        return False

    def isNumber(self, c):
        if ('0' <= c and '9' >= c):
            return True
        else:
            return False
    
    def evaluateExpression(self):
        
        self.expressions = self.expressions.replace(" ", "")
        self.expressions = self.expressions.replace(")(", ")*(")
        self.expressions = self.expressions.replace("(+", "(")
        self.expressions = self.expressions.replace("(-", "(0-")

        if (self.expressions.startswith("+")):
            self.expressions = self.expressions.removeprefix("+")

        if (self.expressions.startswith("-")):
            self.expressions = '0' + self.expressions
        
        i = 0
        while(i < (len(self.expressions) - 1)):

            if self.isNumber(self.expressions[i]):

                if (self.isUnknown(self.expressions[i + 1])):
                    self.expressions = self.expressions[:i+1] + '*' + self.expressions[i+1:]
                    i += 1

                if (self.expressions[i+1] == '('):
                    self.expressions = self.expressions[:i+1] + '*' + self.expressions[i+1:]
                    i += 1

            elif (self.isUnknown(self.expressions[i])):

                if (self.expressions[i+1] == "("):
                    self.expressions = self.expressions[:i+1] + '*' + self.expressions[i+1:]
                    i += 1

            elif (self.expressions[i] == ")"):

                if (self.isUnknown(self.expressions[i + 1])):
                    self.expressions = self.expressions[:i+1] + '*' + self.expressions[i+1:]
                    i += 1
                if (self.isNumber(self.expressions[i + 1])):
                    self.expressions = self.expressions[:i+1] + '*' + self.expressions[i+1:]
                    i += 1
            i += 1
        del i
        self.tokenize()

        counter = 0
        while (counter < len(self.tokens)):

            token = str(self.tokens[counter])
            if (token[0] == '+' or token[0] == '-'):
                while (len(self.operatorStack) != 0 and (self.operatorStack[-1] == '+'or
                self.operatorStack[-1] == '-' or
                self.operatorStack[-1] == '*' or
                self.operatorStack[-1] == '/' )):
                    self.processAnOperator()
                self.operatorStack.append(token[0])
            elif (token[0] == '*' or token[0] == "/"):
                while (len(self.operatorStack) != 0 and (self.operatorStack[-1] == '*' or self.operatorStack[-1] == '/' )):
                    self.processAnOperator()
                self.operatorStack.append(token[0])
            elif (token[0] == '('):
                self.operatorStack.append(token[0])
            elif (token[0] == ')'):
                while(self.operatorStack[-1] != '('):
                    self.processAnOperator()
                self.operatorStack.pop()
            else:
                if ('0' <= token[0] and '9' >= token[0]):
                    if ('.' in token):
                        self.operandStack.append(LinearCoefficient(self.toRational(token), self.unknownChars))
                    else:
                        token = int(token)
                        self.operandStack.append(LinearCoefficient(Fraction(token, 1), self.unknownChars))
                else:
                    self.operandStack.append(LinearCoefficient(Fraction(1,1), token[0], self.unknownChars))
            counter += 1
        
        counter = 0
        while (counter < len(self.operatorStack)):
            self.processAnOperator()
        return self.operandStack.pop()
    
    def processAnOperator(self):
        op = self.operatorStack.pop()
        op1 = self.operandStack.pop()
        op2 = self.operandStack.pop()
        if (op == '+'):
            self.operandStack.append(op2.add(op1))
        elif (op == '-'):
            self.operandStack.append(op2.subtract(op1))
        elif (op == '*'):
            self.operandStack.append(op2.multiply(op1))
        elif (op == '/'):
            self.operandStack.append(op2.divide(op1))
    

    def toRational(self, token):
        decimal = str(token)
        decimal = decimal.strip()
        while (decimal.endswith("0")):
            decimal = decimal[:-1]
        decimalPoint = len(decimal) - decimal.index('.')
        decimals = '1'
        counter = 0
        while(counter < decimalPoint):
            decimals += '0'
            counter += 1
        temp  = int(decimals)
        token = token.replace(".", "")
        token = int(token)
        return Fraction(token, temp)  
    
    def tokenize(self):

        delimiters = '()+-/*'
        token = list()

        for c in (self.expressions):
            if (c != '=' and not c in delimiters and c != ' '):
                token.append(c)
            elif(c in delimiters and c != ' '):
                if (len(token) >= 1):
                    temp = ''
                    for a in token:
                        temp += a
                    self.tokens.append(temp)
                    del temp
                self.tokens.append(c)
                token = list()

        if (len(token) > 0):
            temp = ''
            for c in token:
                temp += c
            self.tokens.append(temp)
            
        del temp
        del token
        del delimiters      

class LinearCoefficient(CoefficientFactory):
    
    def __init__(self, *args):

        checker = type('str')
        argsType = type(args[1])

        if len(args) == 3 and (argsType != checker):
            self.number = args[0]
            self.unknown = args[1]
            self.unknownChar = args[2]
        elif len(args) == 3:
            self.unknownChar = args[2]
            self.unknown = list()
            self.number = Fraction(0,1)
            counter = 0
            while (counter < len(self.unknownChar)):
                self.unknown.append(None)
                counter += 1
            counter = 0
            while(counter < len(self.unknownChar)):
                if (self.unknownChar[counter] == args[1]):
                    self.unknown[counter] = args[0]
                else:
                    self.unknown[counter] = Fraction(0,1)
                counter += 1

        elif len(args) == 2 :
            self.unknownChar = args[1]
            self.number = args[0]
            self.unknown = list()
            counter = 0
            while(counter < len(self.unknownChar)):
                self.unknown.append(Fraction(0, 1))
                counter += 1
        
        del checker
        del argsType

    def add(self, icoefficient):
        unk = list()
        counter = 0
        while (counter < len(self.unknown)):
            unk.append(self.unknown[counter] + icoefficient.unknown[counter])
            counter += 1
        c = LinearCoefficient((self.number + icoefficient.number), unk, self.unknownChar)
        return c
    
    def subtract(self, icoefficient):
        unk = list()
        counter = 0
        while (counter < len(self.unknown)):
            unk.append(self.unknown[counter] - icoefficient.unknown[counter])
            counter += 1
        c = LinearCoefficient((self.number - icoefficient.number),unk, self.unknownChar)
        return c
    
    def multiply(self, icoefficient):
        if (icoefficient.isPureNumber()):
            unk = list()
            counter = 0
            while (counter < len(self.unknown)):
                unk.append(self.unknown[counter] * icoefficient.number)
                counter += 1
            c = LinearCoefficient(self.number * icoefficient.number, unk, self.unknownChar)
            return c
        elif (self.isPureNumber()):
            unk = list()
            counter = 0
            while (counter < len(self.unknown)):
                unk.append(icoefficient.unknown[counter] * self.number)
                counter += 1
            c = LinearCoefficient(icoefficient.number * self.number, unk, self.unknownChar)
            return c
        else:
            raise Exception("Incorrect Linear Equation")
    
    def divide(self, icoefficient):
        if (not icoefficient.isPureNumber()):
            raise Exception("Incorrect Linear Equation")
        unk = list()
        counter = 0
        while (counter < len(self.unknown)):
            unk.append(self.unknown[counter] / icoefficient.number)
        c = LinearCoefficient(self.number * icoefficient.number, unk, self.unknownChar)
        return c
    
    def isPureNumber(self):
        counter = 0
        while (counter < len(self.unknown)):
            if (self.unknown[counter].numerator != 0):
                return False
            counter += 1
        return True

class Matrix:
    
    def __init__(self, rational, n):
        self.matrix = rational
        self.n = int(n)
    
    def solve(self):
        
        k = 0
        while (k < self.n):
            if (self.matrix[k][k].numerator == 0):
                self.changeRow(self.n, k, self.matrix)
            i = 0

            while (i < self.n):    
                temp = self.matrix[i][k]
                j = 0
                while (j < self.n + 1):
                    if (i < k):
                        break
                    if (temp.numerator == 0):
                        continue
                    if (temp.numerator != 1):
                        self.matrix[i][j] = self.matrix[i][j] / temp
                    if (i > k):
                        self.matrix[i][j] = self.matrix[i][j] - self.matrix[k][j]
                    j += 1
                i += 1
            k+=1

        result = list()
        counter = 0
        while(counter < self.n):
            result.append(None)
            counter += 1
        counter = self.n - 1
        while (counter >= 0):
            temp = self.matrix[counter][self.n]
            j = self.n - 1
            while (j >= 0):
                if (counter < j) and (self.matrix[counter][j] != 0):
                    temp = temp - (result[j] * self.matrix[counter][j])
                j -= 1
            temp = temp / self.matrix[counter][counter]
            result[counter] = temp
            counter -= 1
        return result

    def changeRow(self, n, k, matrix):
        n = int(n)
        k = int(k)
        temp = list()
        counter = k
        while(counter < n):
            if (counter + 1 == n) and (matrix[k][k] == 0):
                if (matrix[k][n] == 0):
                    raise Exception('Infinite Solutions Found')
                else:
                    raise Exception('No Solution Found!')
            j = 0
            while (j < n):
                temp[j] = matrix[k][j]
                matrix[k][j] = matrix[counter + 1][j]
                matrix[counter + 1][j] = temp[j]
                j += 1
            if (matrix[k][k] != 0):
                return
            counter+=1

class LinearEquation(AlgebraFactory):
    
    def solve (unknowns, unknownc, lines):
        matrix = [[[Fraction(0,1)] for i in range(unknowns + 1)] for j in range(unknowns)]
        counter = 0
        while(counter < unknowns):
            try:
                expression = str(lines[counter])
                equations = expression.split("=")
                e = EvaluateLinearEquations(equations[0], unknownc)
                coefficient1 = e.evaluateExpression()
                e = EvaluateLinearEquations(equations[1], unknownc)
                coefficient2 = e.evaluateExpression()
                j = 0
                while (j < unknowns):
                    matrix[counter][j] = coefficient1.unknown[j] - coefficient2.unknown[j]
                    j += 1
                matrix[counter][unknowns] = coefficient2.number - coefficient1.number
            except:
                raise Exception('Error at parsing line')
            counter += 1
        m = Matrix(matrix, unknowns)
        return m.solve()