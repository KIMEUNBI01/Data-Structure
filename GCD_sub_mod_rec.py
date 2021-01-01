# 빼기
def gcd_sub(a, b):
	while a*b != 0 : #두 수중 하나가 0이 되기 전까지 빼기를 반복한다
		if a > b :
			a = a - b
		else:
			b = b - a
			
	return a + b

# 나누기
def gcd_mod(a, b):
	while a*b != 0 : #두 수중 하나가 0이 되기 전까지 나누기를 반복한다
		if a > b :
			a = a % b
		else:
			b = b % a
			
	return a + b

# 재귀
def gcd_rec(a, b): 
	if b == 0:
		return a
	else:
		return gcd_rec(b, a % b) #두 수중 하나가 0이 되기 전까지 gcd_rec(a, b)를 반복한다
	
# a, b를 입력받는다
a, b = map(int, input().split())

# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)

# gcd_sub, gcd_mod, gcd_rec의 값을 각각 출력한다
print(x, y, z)