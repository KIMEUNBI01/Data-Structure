class Stack:
	def __init__(self):
		self.data = []

	def push(self,x): 
		self.data.append(x)

	def pop(self):
		data_length=len(self.data)
		# 스택이 비어있을땐 에러메세지 출력
		if data_length < 1:
			#print("Stack is empty")
			return False
		# 가장 위에 있는 data 삭제
		else : 
			self.data.pop()

	def __len__(self):
		return len(self.data)
	
	#def isEmpty(self):
		#if self: return True   ##비어있으면 True
		#else: return False   ##아니면 False	
	
# pseudo code
def parChecker(parSeq):
	S = Stack()
	for p in parSeq:
		if p == '(': S.push(p)
		elif p == ')': S.pop()
		else: print("Not Allowed Symbol")
	if len(S) > 0: return False
	else: return True

print(parChecker(input()))
