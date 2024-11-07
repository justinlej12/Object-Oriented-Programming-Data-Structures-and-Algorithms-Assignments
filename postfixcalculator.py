# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None :
            return True
        return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        counter = 0
        var = self.top
        while var:
            counter += 1
            var = var.next
        return counter

    def push(self, value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == False :
            popval = self.top.value
            self.top = self.top.next
            return popval
        else:
            return None

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == False :
            return self.top.value
        else:
            return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        #tests to see if txt can be casted to a float
        try:
            float(txt)
            return True
        #if there is a value error, return false
        except ValueError:
            return False

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + [ 1 + 4 ]')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''
        # YOUR CODE STARTS HERE
        precedence = {'(': 0, '[': 0, '{': 0, '<': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        #utilizes stack from the previous part
        prevstack = Stack() 
        postfix_expr = []
        #added this later to make sure that exponents are taken into account from right to left ('7 ^ 2 ^ 3' case)
        exponentiation = {'^'}
        #these are the operators that are supported by the calculator
        supported_operators = '+-*/^'
        space = False 
        number_count = 0 
        operators = False
        copy = txt
        #if the first character in the string is a space, remove it
        if txt[0] == " ": 
            copy = txt[1:]
        for i in copy: 
            if self._isNumber(i) == True: 
                number_count += 1 
            elif i == " ": 
                space = True 
            elif i in precedence: 
                operators = True
        #checks to see if there are no operators, and if so returns none
        if space == True and number_count >= 2 and operators == False:
            return None
        #test case for >>> x._getPostfix('2    5')
        for i in range(len(txt)-2):
            if txt[i + 1] == " " and txt[i + 2] == " ":
                return None
        #check to see if there is an incomplete expression ie. the ('25 + test case')
        operatorExists = False
        numberAfterOperatorExists = False
        i=0
        while i<len(txt):
            if txt[i] in precedence:
                operatorExists = True
                j = i
                while j < len(txt):
                    if txt[j].isdigit() or txt[j] == '.':
                        numberAfterOperatorExists = True
                        j = len(txt)
                    j += 1
            i += 1
        if operatorExists and not numberAfterOperatorExists:
            return None
        #check to see if there are negative numbers in an expression
        negNum = False
        newtxt = txt
        for i in range(len(txt)): 
            if txt[i]=='-' and i+1 < len(txt) and self._isNumber(txt[i+1]):
                newtxt = txt[0:i] + "@" + txt[i+1:] 
                negNum = True
            elif txt[i]=='-' and i>=2 and txt[i-2] in supported_operators:
                return None
        if negNum:
            infix_expr=''.join(newtxt.split())
        else:
            infix_expr=''.join(txt.split())
        #check for unbalanced parenthesees
        paren_mapping = {'(': ')', '[': ']', '{': '}', '<': '>'}
        paren_stack = []
        for char in infix_expr:
            if char in paren_mapping.keys():
                paren_stack.append(char)
            elif char in paren_mapping.values():
                if not paren_stack or paren_mapping[paren_stack.pop()] != char:
                    return None
        if paren_stack:
            return None
        #implied multiplication 
        for i in range(len(infix_expr)-1): 
            curr, next_char = infix_expr[i], infix_expr[i+1] 
            if (curr.isdigit() or curr.isalpha() or curr in paren_mapping.values()) and next_char in paren_mapping.keys():
                infix_expr = infix_expr[:i+1] + "*" + infix_expr[i+1:]

            elif curr in paren_mapping.values() and (self._isNumber(next_char) or next_char in paren_mapping.keys()):
                infix_expr = infix_expr[:i+1] + "*" + infix_expr[i+1:]
        i = 0
        #iterate through chars in  infix expression
        while i < len(infix_expr):
            char = infix_expr[i]
            #operand check
            if char.isdigit() or char == '.' or char == '@':
                operand = char
                i += 1
                while i < len(infix_expr) and (infix_expr[i].isdigit() or infix_expr[i] == '.'):
                    operand += infix_expr[i]
                    i += 1
                postfix_expr.append(operand)
                #more implied multi
                if i < len(infix_expr) and infix_expr[i] in paren_mapping.keys():
                    prevstack.push('*')
            #exponentiation check
            elif char in exponentiation:
                while len(prevstack) > 0 and prevstack.peek() != '(' and precedence[char] < precedence[prevstack.peek()]:
                    postfix_expr.append(prevstack.pop())
                prevstack.push(char)
                i += 1
            #operator check
            elif char in supported_operators:
                if i == 0 or infix_expr[i - 1] in supported_operators or infix_expr[i - 1] == '(':
                    if char == '-':
                        postfix_expr.append(0)
                    else:
                        return None
                else:
                    while len(prevstack) > 0 and prevstack.peek() != '(' and precedence[char] <= precedence[prevstack.peek()]:
                        postfix_expr.append(prevstack.pop())
                    prevstack.push(char)
                i += 1
            #parenthesees
            elif char in ['(', '[', '{', '<']:
                prevstack.push(char)
                i += 1
            elif char in [')', ']', '}', '>']:
                top_char = prevstack.pop()
                while top_char not in ['(', '[', '{', '<']:
                    postfix_expr.append(top_char)
                    top_char = prevstack.pop()
                i += 1
            #space check
            elif char == ' ':
                i += 1
            else:
                return None
        #check for remaining operators
        while len(prevstack) > 0:
            top_char = prevstack.pop()
            if top_char in ['(', '[', '{', '<']:
                return None
            postfix_expr.append(top_char)
        #subtract check
        tf = False
        for i in range(len(postfix_expr)):
            if postfix_expr[i] == 0:
                tf = True
                index = i
        if tf:
            postfix_expr.remove(0)
            second = postfix_expr[index]
            first = '-'
            postfix_expr[index] = first + second
        #string assembly
        final_str = ''
        for i in postfix_expr:
            if self._isNumber(i):
                i = float(i)
                final_str = final_str + str(i) + " "
            else:
                final_str = final_str + i + " "
        #'@' placeholder"
        final_format = ''
        for i in range(len(final_str)):
            if final_str[i] == '@':
                floated = float(final_str[i + 1])
                final_format = final_str[0:i] + "-" + str(floated) + final_str[i + 2:]
        #return of final str
        if final_format:
            return final_format[:-1]
        else:
            return final_str[:-1]

    def evaluate_operator(self, leftop, rightop, operator):
        if operator == "+":
            return leftop + rightop
        elif operator == "-":
            return leftop - rightop
        elif operator == "*":
            return leftop * rightop
        elif operator == "/":
            return leftop / rightop
        elif operator == '^': 
            return leftop ** rightop           

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * { 5 - 3 ^ 2 } + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * [ 4 ] ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            return None
        calcStack = Stack()  
        expr = self.__expr 
        temporary_expr = self._getPostfix(expr) 
        if temporary_expr == None: 
            return None
        post_expr = temporary_expr.split()
        if post_expr == None: 
            return None 
        #loop through each token
        for token in post_expr:
            #if the token is an operator, pop the last two values from the stack then push the result back onto the stack
            if token in "+-*/^":
                rightop = calcStack.pop()
                leftop = calcStack.pop()
                result = self.evaluate_operator(leftop, rightop, token)
                calcStack.push(result)
            # if token is a number, push it onto the stack
            else:
                calcStack.push(float(token))
        #final result should be the only value left on the stack
        return calcStack.pop()

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if word is None: 
            return None 
        if word[0].isalpha() == False: 
            return False 
        for i in word[1:]: 
            if not (i.isalpha() or i.isdigit() or i =="_"): 
                return False
        return True 
       
    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        for i in self.states: 
            if i in expr: 
                value = str(self.states[i]) 
                expr = expr.replace(i, value) 
        for j in expr: 
            if self._isVariable(j): 
                return None 
        return expr
    
    def calculateExpressions(self):
        #initialization
        self.states = {} 
        big_dict = {} 
        calc_obj = Calculator()     
        exp_track = self.expressions.split(';')
        #iterate through each of the expressions in the list
        for expression in exp_track:
            #check if there is assignment in the expression
            if "=" in expression:
                if self.states:
                    variable, value = expression.split('=')
                    #check to see if the variable is a number
                    if Calculator._isNumber(self, value) == True:
                        self.states[variable[0:-1]] = float(value)
                    #if not number replace variable and calculate value
                    else:
                        replaced_expression =self._replaceVariables(value)
                        calc_obj.setExpr(replaced_expression) 
                        calc_value = calc_obj.calculate 
                        self.states[variable[0:-1]] = calc_value
                else: 
                    number = False
                    variable, value = expression.split('=')
                    #check to see if value contains numbers
                    for i in value: 
                        if Calculator._isNumber(self,i) == True: 
                            number=True   
                    if number == True: 
                        replaced_expression=self._replaceVariables(value)
                        calc_obj.setExpr(replaced_expression) 
                        calc_value= calc_obj.calculate 
                        self.states[variable[0:-1]] = calc_value
                if self._isVariable(str(variable[0:-1])) == False: 
                    self.states = {} 
                    return None   
                big_dict[expression]=dict(self.states)
            else: 
                result = expression.strip("return")
                replace_result = self._replaceVariables(result)
                calc_obj.setExpr(replace_result)
                calculator=calc_obj.calculate
                if calculator == None: 
                    self.states = {} 
                    return None      
        big_dict["_return_"] = calculator 
        return big_dict

def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples(Stack, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()