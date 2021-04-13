class Stack:	
	def __init__(self):
		self.items = []
	
	def push(self, val):
		self.items.append(val)
	
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")

	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")

	def __len__(self):
		return len(self.items)

	def isEmpty(self):
		return self.__len__() == 0	
	
def get_token_list(expr):
	token_list = [] #expr을 연산자와 피연산자로 나눈 후 담을 리스트
	index = 0 #문자열로 되어 있는 한 자리 이상의 실수를 하나의 실수인 피연산자로 저장하기 위해 필요한 인덱스
	
	while index < len(expr): #문자열의 길이만큼 반복
		op = expr[index] #expr의 첫 인덱스 부터 시작
		if op in'()+-*/^': #연산자, 괄호
			token_list.append(op) #token_list에 append
			index += 1 #인덱스 증가
			
		elif op.isdigit() or op == ".": #숫자, '.'
			j = index + 1 #숫자와 '.' 다음에 오는 문자열이 연산자인지 피연산자인지 판단하기 위해 필요한 인덱스
			while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'): #j가 문자열의 길이보다 작을 때, 숫자이거나 '.'이면 즉, 다음 연산자가 나오기 전까지 반복
				j += 1 #j 다음에 오는 문자열이 피연산자이면 1증가
			operand = str(float(expr[index:j])) #피연산자는 float 형식으로 변환해야하므로 float로 변환하고 형식을 맞추기 위해 다시 str로 변환
			index = j #인덱스 증가
			token_list.append(operand) #token_list에 append
			
		elif op.isspace(): #' '
			index += 1  #인덱스 증가
			
		else: #연산자, 괄호, 숫자, '.', ' ' 이외에는 잘못된 입력 -> IndexError
			print("IndexError")
			break
			
	return token_list #expr을 연산자와 피연산자로 나눈 후 담은 token_list 리스트 리턴

def infix_to_postfix(token_list):
	opstack = Stack() #infix의 수식인 token_list를 postfix로 변환 하기 위해 필요한 stack
	outstack = [] #postfix로 변환한 수식을 저장할 리스트
	
	#연산자의 우선순위 설정
	prec = {}
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3

	for token in token_list:
		if token == '(': #'('이면 스택에 push
			opstack.push(token)
		elif token == ')': #')' 이면 '('가 나올때까지 pop
			while opstack.top() != '(':
				outstack.append(opstack.pop())
			opstack.pop()
		elif token in '+-/*^': #+-/*^ 연산자이면
			if opstack.isEmpty(): #스택이 비어있다면 스택에 push
				opstack.push(token)
			else: #스택이 비어있지 않다면 비교
				while not opstack.isEmpty(): #스택에 값이 존재할 때 까지 반복
					if prec[opstack.top()] >= prec[token]: #스택 안에 있는게 우선 순위가 높으면 꺼냄
						outstack.append(opstack.pop())
					else:
						break
				opstack.push(token)
		else: #피연산자이면
			outstack.append(token)
			
	#opstack에 남은 모든 연산자를 pop 후 outstack에 append
	while not opstack.isEmpty():
		outstack.append(opstack.pop())
	
	return outstack #token_list를 Postfix로 변환한 결과를 담은 outstack 리스트를 리턴

#Postfix 계산 
#허용연산자 = 이항연산자(+,-,*,/,^)
def compute_postfix(token_list):
	opstack = Stack() #Postfix를 계산하기 위한 stack

	for token in token_list:
		#연산자면
		if token == '+': #덧셈
			a = opstack.pop()
			b = opstack.pop()
			opstack.push( a + b )
		elif token == '-': #뺄셈
			a = opstack.pop()
			b = opstack.pop()
			opstack.push( b - a )
		elif token == '*': #곱셈
			a = opstack.pop()
			b = opstack.pop()
			opstack.push( a * b )
		elif token == '^': #제곱
			a = opstack.pop()
			b = opstack.pop()
			opstack.push( b ** a )
		elif token == '/': #나눗셈
			a = opstack.pop()
			b = opstack.pop()
			opstack.push( b / a )
		else: #피연산자면 스택에 float 형식으로 push	
			opstack.push(float(token))
			
	return float(opstack.pop()) #postfix 형식의 token_list에 대한 계산 값을 리턴

expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)