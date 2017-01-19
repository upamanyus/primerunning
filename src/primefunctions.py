class PrimeFunctions:

    def __init__(self,textName):
        primeFile = open(textName)
        primeStrings = primeFile.read().split()
        primeFile.close()
        self.primes=[ int(num) for num in primeStrings ] 

    def runningStep(self, a, q, n):
        index = 0
        while self.primes[index] <= n:
            index += 1
        index -= 1
        if self.primes[index] % q == a:
            return 1
        else:
            return 0

    def runningSum(self, a, q, n):
        sum = 0
        for i in range(1,n+1):
            sum += self.runningStep(a,q,i)
        return sum

    def walkingStep(self, a,q,p):
        if p % q == a:
            return 1
        else:
            return 0

    def walkingSum(self, a,q,x):
        sum = 0
        index = 0
        while self.primes[index] <= x:
            sum += self.walkingStep(a,q,self.primes[index])
            index += 1
        return sum

    def prevCongPrimes(self, a,q,x):
        count = 0
        index = 0
        while self.primes[index] <= x:
            if primes[index] % q == a:
                count += 1
        return count
