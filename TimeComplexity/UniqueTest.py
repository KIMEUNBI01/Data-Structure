import random, time

def unique_n2(A):
	for i in range(0, len(A)):   #n
		for j in range(i+1, len(A)):   #n-1
			#리스트의 자신을 제외한 값들 중 자신과 같은 값이 있는지 확인한다 
			if A[i] == A[j]: #만약 A[i]와 A[j]가 같다면 중복된 수가 존재한다는 의미이다 
				return 'NO' #'NO'를 출력하기 위해 리턴한다   #1
	#A의 값들이 서로 다르다면
	return 'YES' #'YES'를 출력하기 위해 리턴한다   #1
	# -> O(n^2)
	
def unique_nlogn(A):
	A.sort()   #nlogn
	for i in range(1, len(A)):   #n-1
		#오름차순으로 정렬했으므로 i-1의 값이 자신과 같은지 확인한다.
		if A[i] == A[i-1]: #만약 A[i]와 A[i-1]이 같다면 중복된 수가 존재한다는 의미이다 
			return 'NO' #'NO'를 출력하기 위해 리턴한다   #1
	#A의 값들이 서로 다르다면
	return 'YES' #'YES'를 출력하기 위해 리턴한다   #1
  # -> O(nlogn)

def unique_n(A):
	#A의 값들이 -n부터 n사이의 값들이므로 중복이 있는지 확인하기 위해 set을 실시한다
	B = list(set(A)) #n	
	#만약 A의 값들 중 중복된 수가 있으면 하나만 저장되기 때문에 A와 B의 길이를 비교해본다
	if len(A) != len(B): #만약 A와 B의 길이가 다르면 중복된 수가 존재한다는 의미이다 
		return 'NO' #'NO'를 출력하기 위해 리턴한다   #1
	#A의 값들이 서로 다르다면
	return 'YES'  #'YES'를 출력하기 위해 리턴한다   #1
  # -> O(n)
	
	
n = int(input()) # input: 값의 개수 n
A = random.sample(range(-n, n+1), n) # -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
# 동시에 각 함수의 실행 시간을 측정해본다
# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다
s1 = time.process_time()
print(unique_n2(A)) #unique_n2(A)호출 & 유일성 결과 출력
e1 = time.process_time()

s2 = time.process_time()
print(unique_nlogn(A)) #unique_nlogn(A)호출 & 유일성 결과 출력
e2 = time.process_time()

s3 = time.process_time()
print(unique_n(A)) #unique_n(A)호출 & 유일성 결과 출력
e3 = time.process_time()

print("unique_n2(A) 수행시간 =", e1 - s1) #unique_n2(A)의 수행시간
print("unique_nlogn(A) 수행시간 =", e2 - s2) #unique_nlogn(A)의 수행시간
print("unique_n(A) 수행시간 =", e3 - s3) #unique_n(A) 수행시간
