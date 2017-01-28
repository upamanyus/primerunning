class PrimeFunctions:

    def __init__(self, textName):
        primeFile = open(textName)
        primeStrings = primeFile.read().split()
        primeFile.close()
        self.maxValue = int(primeStrings[0])
        self.primes = [int(num) for num in primeStrings[1:]]

    def runningStep(self, a, q, n):
        """returns 0 if largest prime less than or equal to n is congruent to a mod q, 1 otherwise"""
        if n > self.maxValue:
            raise RuntimeError("Input outside of range")
        index = 0
        if n < 2:
            return 0
        while self.primes[index+1] < n:
            index += 1
        if self.primes[index] % q == a:
            return 1
        else:
            return 0

    def runningSum(self, a, q, values):
        """returns the sum of the runningStep from 1 to n"""
        if values[len(values)-1] > self.maxValue:
            raise RuntimeError("Input outside of range")
        output = []
        index = 0
        sum = 0
        for i in range(1, values[len(values) - 1] + 1):
            sum += self.runningStep(a, q, i)
            if i == values[index]:
                output.append(sum)
                index += 1
        return output

    def walkingStep(self, a, q, p):
        """returns 1 if p is congruent to a mod q, 0 otherwise"""
        if p > self.maxValue:
            raise RuntimeError("Input outside of range")
        if p % q == a:
            return 1
        else:
            return 0

    def walkingSum(self, a, q, n):
        """returns number of primes congruent to a mod q between for primes less than x"""
        if n > self.maxValue:
            raise RuntimeError("Input outside of range")
        sum = 0
        index = 0
        while index < len(self.primes) and self.primes[index] <= n:
            sum += self.walkingStep(a, q, self.primes[index])
            index += 1
        return sum
