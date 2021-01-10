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

# Postfix 계산 
# 1. 허용연산자 = 이항연산자(+,-,*,/,^)
# 2. 문자열의 연속된 두 항 사이에는 모두 공백 하나 ' '가 있음)
def compute_postfix(postfix):
	S = Stack()
	operators = ['+' , '-' , '*' , '/' , '^']
	
	for token in postfix:
		if '0' <= token <= '9':
			S.push(float(token))
			
		elif token == '+': #뎃셈
			n1 = S.pop()
			n2 = S.pop()
			S.push(n2 + n1)
		elif token == '-': #뺄셈
			n1 = S.pop()
			n2 = S.pop()
			S.push(n2 - n1)
		elif token == '*': #곱셈
			n1 = S.pop()
			n2 = S.pop()
			S.push(n2 * n1)
		elif token == '/': #나눗셈
			n1 = S.pop()
			n2 = S.pop()
			S.push(float(n2 / n1))
		elif token == '^': #제곱
			n1 = S.pop()
			n2 = S.pop()
			S.push(float(n2 ** n1))
		else:
			S.push(token)
			
	return S.pop()

res = compute_postfix(input().split())
print('%.4f ' %res) #소수점 이하 4자리까지 출력
