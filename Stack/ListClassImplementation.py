class myList():
	def __init__(self):
		self.capacity = 2 # myList의 용량 (저장할 수 있는 원소 개수)
		self.n = 0 # 실제 저장된 값의 개수
		self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

	def __len__(self):
		return self.n
	
	def __str__(self):
		return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'
        
    def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
		if k >= self.n: #실제 저장된 값의 개수 보다 k값이 크거나 같으면 IndexError 발생
			raise IndexError	
		return self.A[k]

	def __setitem__(self, k, x):# k번째 칸에 값 x 저장
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
		if k >= self.n: #실제 저장된 값의 개수 보다 k값이 크거나 같으면 IndexError 발생
			raise IndexError	
		self.A[k] = x

	def change_size(self, new_capacity):
		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
		B = [None] * new_capacity #new_capacity의 크기의 리스트 B를 만듬
		for i in range(self.n): #실제 저장된 값의 개수만큼 self.A의 값을 B로 옮김
			B[i] = self.A[i]
		del self.A
		self.A = B
		self.capacity = new_capacity
	
	def append(self, x):
		if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
			self.change_size(self.capacity * 2)
		self.A[self.n] = x # 맨 뒤에 삽입
		self.n += 1 # n 값 1 증가

	def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
		#실제 저장된 값의 개수가 0이거나 실제 저장된 값의 개수 보다 k값이 크거나 같으면 IndexError 발생
		if self.n == 0 or k >= self.n: # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: 
			raise IndexError
		if self.capacity >= 4 and self.n <= self.capacity//4: # 실제 key 값이 전체의 25% 이하면 halving
			self.change_size(self.capacity//2)
		# k 값이 주어진 경우와 주어지지 않은 경우를 구별
		if k == -1 : #k 값이 주어지지 않은 경우는 k가 -1로 들어옴
			k = self.n -1 #가장 오른쪽 값 k의 인덱스 = self.n - 1 (self.n이 실제 저장된 값의 개수 이므로)
		x = self.A[k]
		# A[k]의 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
		for i in range(k, self.n-1): #k번째 부터 끝까지
			self.A[i] = self.A[i+1]
		self.n -= 1 # n 값 1 감소
		return x

	def insert(self, k, x):
		# 주의: k 값이 음수값일 수도 있음
		# k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
		# k의 범위가 올바르지 않으면 IndexError 발생시킴
		if k >= self.n: #실제 저장된 값의 개수 보다 k값이 크거나 같으면 IndexError 발생
			raise IndexError
		# self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
		if self.n == self.capacity:
			self.change_size(self.capacity*2)
		# A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
		for i in range(self.n, k, -1): #끝부터 k번째까지
			self.A[i] = self.A[i-1]
		self.A[k] = x # k번째 칸에 값 x 저장
		self.n += 1 # n 값 1 증가

	def size(self): #L의 크기 리턴
		return len(self.A)

L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get': # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set': # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")git commit -m 'Stack'