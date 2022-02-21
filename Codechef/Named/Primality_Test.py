ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]


from math import sqrt

def isPrime(n):

	if (n <= 1):
		return False

	
	for i in range(2, int(sqrt(n))+1):
		if (n % i == 0):
			return False

	return True




for _ in range(ii()):
    n = ii()
    print("yes" if isPrime(n) else "no")