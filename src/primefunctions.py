class PrimeFunctions:

    def __init__(self,textName):
        primeFile = open(textName)
        primeStrings = primeFile.read().split()
        primeFile.close()
        self.primes=[ int(num) for num in primeStrings ] 

    def runningStep(self, a, q, n):
        """returns 0 if largest prime less than or equal to n is congruent to a mod q, 1 otherwise"""
        index = 0
        if n < 2:
            return 0
        while self.primes[index+1] < n:
            index += 1
        if self.primes[index] % q == a:
            return 1
        else:
            return 0

    def runningSum(self, a, q, n):
        """returns the sum of the runningStep from 1 to n"""
        sum = 0
        for i in range(1,n+1):
            sum += self.runningStep(a,q,i)
        return sum

    def walkingStep(self, a,q,p):
        """returns 1 if p is congruent to a mod q, 0 otherwise"""
        if p % q == a:
            return 1
        else:
            return 0

    def walkingSum(self, a,q,x):
        """returns number of primes congruent to a mod q between for primes less than x"""
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
