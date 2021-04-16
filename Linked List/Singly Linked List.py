class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None

	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		node = Node(key)
		node.next = self.head
		self.head = node # head 노드가 바뀜head 노드가 바뀜
		self.size += 1
	
	def pushBack(self, key):
		v = Node(key)
		if self.head == None: # empty list --> v becomes a head!
			self.head = v
		else:
			tail = self.head
			while tail.next is not None: # follow links until tail
				tail = tail.next
			tail.next = v
		self.size += 1
	
	def popFront(self): 
		# head 노드의 값 리턴. empty list이면 None 리턴
		if self.head == None:
			return None
		else:
			v = self.head
			key = v.key
			self.head = self.head.next
			self.size -= 1
			del v
			return key
	
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.head == None: 	# empty list (nothing to pop)
			return None
		else:
			# tail 노드와 그 전 노드인 previous를 찾는다
			prev = None
			tail = self.head
			while tail.next is not None: # 한 노드씩 진행
				prev = tail
				tail = tail.next
			# 만약 리스트에 노드가 하나라면 그 노드가 head이면서 동시에 tail임
			# 그런 경우라면 tail을 지우면 빈 리스트가 되어 head = None으로 수정해야함!
			if self.size == 1: 	# 또는 if previous == None:
				self.head = None
			else:
				prev.next = tail.next # previous가 새로운 tail이 됨!
			key = tail.key
			self.size -= 1
			del tail
			return key
	
	def search(self, key):
		# key 값을 갖는 노드 리턴. 없으면 None 리턴
		v = self.head
		while v is not None:
			if v.key == key:
				return v
			v = v.next
		return None
	
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!
		if x == None or self.size == 0:
			return False
		else:
			if x == self.head:
				self.popFront()
			else:
				previous = self.head
				while previous.next is not x: #노드 x를 찾는다를 찾는다
					previous = previous.next
				previous.next = x.next #노드 x를 삭제한다
				self.size -= 1
			return True
	
	def reverse(self, key):
		#key 값을 갖는 첫번째 노드 x부터 tail노드까지의 노드들을 반대로 뒤집기
		if self.size == 0 or self.size == 1: #empty list이거나 노드가 하나라면 아무일도 하지 않는다
			pass
		
		node = self.search(key)
		if node == None: #key값을 갖는 노드가 없으면 아무일도 하지 않는다
			pass
		
		else:
			index = 1 #뒤집기 시작할 위치를 지정할 인덱스
			v = self.head
			before_key = None
			for i in range (self.size):
				if v.key == key :
						break
				before_key = v #뒤집은 노드들 앞에 연결할 key값을 갖는 첫번째 노드 바로 앞 노드
				v = v.next
				index += 1
				
			if index == 1: #index = 1
				prev = None
				curr = self.head
				
				while curr is not None:
					next = curr.next
					curr.next = prev
					prev = curr
					curr= next
				
				self.head = prev
				
			elif 1 < index < self.size: #1 < index < self.size
				prev = None
				curr = before_key.next
				
				while curr is not None:
					next = curr.next
					curr.next = prev
					prev = curr
					curr= next
				
				before_key.next = prev
				
			elif index == self.size: #key 값을 갖는 첫번째 노드 x가 맨 끝 값이라면 아무일도 하지 않는다
				pass
			
			else: #index <= self.size이라면 아무일도 하지 않는다
				pass	
	
	def findMax(self): 
		#self가 empty이면 None, 아니면 max key 찾은 후, max key 리턴
		if self.size == 0: 	#empty list
			return None
		else:
			curr = self.head
			Max = self.head.key
			while curr is not None:
				if Max < curr.key:
					Max = curr.key
				curr = curr.next
			return Max
		
	def deleteMax(self):
		#self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		if self.size == 0: 	#empty list
			return None
		else:
			Max = self.findMax()
			Max_node = self.search(Max)
			self.remove(Max_node)
			return Max
	
	def insert(self, k, key):
		#head 노드 부터 k번째 노드 다음에 key를 갖는 새로운 노드를 삽입 (k > 0이라고 가정)
		if 0 <= k < self.size: #0 <= k < self.size
			node = self.head 
			for i in range(k-1):
				node = node.next #삽입할 위치 = k-1번째 노드 뒤
			new = Node(key)
			tmp = node.next
			node.next = new
			new.next = tmp
			self.size += 1
			
		else: #노드의 개수가 k개보다 작다면
			self.pushBack(key) #가장 뒤에 삽입

	def size(self):
		return self.size