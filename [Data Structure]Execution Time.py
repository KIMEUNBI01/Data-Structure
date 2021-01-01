import time, random

#A[n]까지의 합
def sum(A, n):
	Nsum = 0
	for i in range (n):
		Nsum += A[i]
	return Nsum;

# n = 1 이상 5000 이하 정수 값 입력
n = int(input("1 <= n <= 5000 : "))

# 리스트 A에 랜덤 정수 값 n개 채움
A = []
for i in range (n):
	A.append(random.randint(0,100))

# sum 함수 호출 + 시간 측정
# 함수의 수행시간을 출력
B = [[n]]
for i in range (n):
	for j in range (n):
		start = time.time()
		B.append(sum(A,j))
		end = time.time()
		print('Execution time :', end - start)
