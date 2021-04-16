class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next

	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
    
def splice(self, a, b, x): # cut [a..b] after x
		if a == None or b == None or x == None: 
			return
		# 1. [a..b] 구간을 잘라내기 
		a.prev.next = b.next
		b.next.prev = a.prev
		# 2. [a..b]를 x 다음에 삽입하기
		x.next.prev = b
		b.next = x.next
		a.prev = x
		x.next = a

	def moveAfter(self, a, x):
		#노드 a를 노드 x 뒤로 move
		DoublyLinkedList.splice(self, a, a, x)

	def moveBefore(self, a, x):
		#노드 a를 노드 x 앞으로 move
		DoublyLinkedList.splice(self, a, a, x.prev)

	def insertBefore(self, k, val):
		#k번째 앞에 insert
		DoublyLinkedList.moveBefore(self, Node(val), k)

	def insertAfter(self, k, val):
		#k번째 뒤에 insert
		DoublyLinkedList.moveAfter(self, Node(val), k)

	def pushFront(self, key):
		#맨 앞에 push
		DoublyLinkedList.insertAfter(self, self.head, key)

	def pushBack(self, key):
		#맨 뒤에 push
		DoublyLinkedList.insertBefore(self, self.head, key)

	def deleteNode(self, x): 
		#x노드 값 delete
		if x == None or x == self.head: 
			return
		x.prev.next, x.next.prev = x.next, x.prev  #노드 x를 리스트에서 분리
		del x
	
	def popFront(self):
		#head 노드의 값 리턴. empty list이면 None 리턴
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			v = self.head.next
		DoublyLinkedList.deleteNode(self, v)
		return v
	
	def popBack(self):
		#tail 노드의 값 리턴. empty list이면 None 리턴
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			v = self.head.prev
		DoublyLinkedList.deleteNode(self, v)
		return v

	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head	#Dummy Node
		if key == v.prev.key:
			return v.prev
		while v.next != self.head:
			if v.key == key:
				return v
			v = v.next
		return None	#search failed

	def first(self):
		#self가 empty이면 None, 아니면 첫번째 값 리턴
		v = self.head
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			return v.next

	def last(self):
		#self가 empty이면 None, 아니면 맨끝값 값 리턴
		v = self.head
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			return v.prev

	def isEmpty(self):
		#self가 empty이면 True, 아니면 False 리턴
		if self.head == self.head.next:
			return True
		else:
			return False
	
	def findMax(self):
		#self가 empty이면 None, 아니면 max key 찾은 후, max key 리턴
		if self.size == 0: # empty list
			return None
		else:
			curr = self.head.next
			Max = curr.key
			while curr.key is not None:
				if Max < curr.key:
					Max = curr.key
				curr = curr.next
			return Max #max key값 리턴

	def deleteMax(self):
		#self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		if self.size == 0: #empty list
			return None
		else:
			Max = self.findMax() #max key값
			Max_node = self.search(Max)
			self.deleteNode(Max_node) #max key값 삭제
		return Max #max key값 리턴

	def sort(self):
		result = [] #가장큰값을 저장할 리스트
		v = self.head
		Max = self.deleteMax() #가장큰값 설정
		while Max is not None: #DoublyLinkedList가 None이 될 때 까지
			result.append(Max) #리스트에 가장큰값 append
			Max = self.deleteMax() #append한 큰값 다음으로 큰값 찾기
		for i in range(len(result)): #리스트의 길이 만큼 즉, DoublyLinkedList의 원소만큼
			self.pushFront(result[i]) #차례대로 pushFront -> 자동으로 오름차순으로 정렬 됨
			i += 1
		return L #정렬된 DoublyLinkedList 리턴
	
	def size(self): 
		#self의 size리턴
		return self.size