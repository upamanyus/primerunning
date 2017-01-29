class PrimeFunctions:
    def __init__(self, textName):
        primeFile = open(textName)
        primeStrings = primeFile.read().split()
        primeFile.close()
        self.maxValue = int(primeStrings[0])
        self.primes = [int(num) for num in primeStrings[1:]]

    def walkingStep(self, a, q, p):
        """Returns 1 if p = a mod q, and 0 otherwise. Assumes that p is not
        larger than self.maxValue."""
        if p % q == a:
            return 1
        else:
            return 0

    def runningStep(self, a, q, n):
        """Returns 0 if largest prime less than or equal to n = a (mod q), and 1
        otherwise. Assumes that n is larger self.maxValue."""
        index = 0
        if n < 2:
            return 0
        while self.primes[index] < n:
            index += 1
            if index >= len(self.primes) or self.primes[index] > n:
                index -= 1
                break
        if self.primes[index] % q == a:
            return 1
        else:
            return 0

    def walkingSumPrimes(self, a, q):
        """Returns the output values of the prime walking function at prime
        coordinates (i.e., the jth entry in the output array corresponds to the
        jth prime number)."""
        sum = 0
        output = [0]
        for p in self.primes[1:]:
            if p % q == a:
                sum += 1
            output.append(sum)
        return output

    def runningSum(self, a, q, n):
        """Returns the prime running function evaluated at n."""
        if n > self.maxValue:
            raise RuntimeError("Number too large")
        sum = 0
        r = self.primes[0]
        for p in self.primes[1:]:
            if p > n:
                sum += (n - r) * self.walkingStep(a, q, r)
                return sum
            sum += self.walkingStep(a, q, r) * (p - r)
            r = p
        return sum + (n - r) * self.walkingStep(a, q, r)

    def runningSumPrimes(self, a, q):
        """Returns the output values of the prime running function at prime
        coordinates (i.e., the jth entry in the output array corresponds to the
        jth prime number)."""
        r = self.primes[0]
        sum = 0
        output = [0]
        for p in self.primes[1:]:
            if r % q == a:
                sum += (p - r - 1)
            if p % q == a:
                sum += 1
            r = p
            output.append(sum)
        return output

    def runningSumPrimesAll(self, q):
        """Returns an array of arrays, where the jth array contains the
        output values of the prime running function j mod q."""
        outputs = [[0] for a in range(q)]  # TODO: Fix the starting coordinate
        sums = [0 for a in range(q)]
        r = self.primes[0]
        for p in self.primes[1:]:
            a = p % q
            sums[a] += 1
            b = r % q
            sums[b] += p - r - 1
            for i in range(q):
                outputs[i].append(sums[i])
            r = p
        return outputs
