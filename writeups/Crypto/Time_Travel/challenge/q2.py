from Crypto.Util import *
import gmpy
import random

def gcd(a,b): 
    if(b==0): 
        return a 
    return gcd(b,a%b)

def giveMeABigNumber():
	return random.randint(0,pow(10,1337))

def encode(x):
	s =''
	for i in str(x):
		s += str(dictionary[i])
	return int(s)

def g(x,e,N):
	t = 1
	i = 0
	while i != e:
		t *= x
		t %= N
		i += 1
	return t

def f(x,k,e,N):
	x = g(x,e,N)
	x *= k
	x %= N
	return x

def giveMeSomeGoodPrimes():
	primes = []
	while len(primes) != 255:
		x = number.getPrime(32)
		if len(str(x)) != 10:
			continue
		else:
			if x in primes:
				continue
			primes.append(x)
	while True:
		g = primes[0]
		phi = 1
		for i in primes:
			phi *= (i-1)
		if gcd(phi,sum(primes)) == 1:
			break
		else:
			primes.pop(0)
			while True:
				x = number.getPrime(32)
				if len(str(x)) != 10:
					continue
				else:
					if x in primes:
						continue
					primes.append(x)
					break			
	return primes

primes = giveMeSomeGoodPrimes()
primes.sort()

flag = 'd4rk{************REDACTED************}c0de'

diff_vec = []

for i in range(1,len(primes)):
	diff_vec.append(primes[i]-primes[i-1])

dictionary = {}

for i in range(255):
	dictionary[chr(i)] = primes[i]

e = sum(primes)
k = 0
N = 1
for i in range(len(primes)):
	k ^= primes[i]
	N *= primes[i]

enc = encode(flag)

myBigNumber = giveMeABigNumber()

i = 0

while i != (myBigNumber):
	enc = f(enc,k,e,N)
	i += 1

print (enc,k,e,N,diff_vec,myBigNumber)




