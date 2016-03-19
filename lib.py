import math
import random

def bin2Gray(x):
    return x ^ x >> 1

def Gray2bin(x):
    maxBits = 17 # requirement
    res = 0
    for i in xrange(maxBits - 1, -1, -1):
        if res == 0 and (x & 1 << i) > 0:
            res = 1 << i
        elif res > 0:
            res |= (x & 1 << i) ^ (res & 1 << i + 1) >> 1
    return res

# @note The function
def Griewank(xs):
    sum = 0
    for x in xs:
        sum += x * x
    product = 1
    for i in xrange(len(xs)):
        product *= math.cos(xs[i] / math.sqrt(i + 1))
    return 1 + sum / 4000 - product

#TODO: fix this
def GriewankKludge(xs):
    return Griewank([xs])

def fitness(xs):
    f = GriewankKludge(xs)
    print 'G({0})={1}'.format(xs, f)
    return f

# @note Size of a population
N = 10

# TODO: do not use lists but numpy arrays (everywhere)
individuals = [None] * N

# Q: why/how should I run initialization on search space?
# @note -655.36 <= x[i] < 655.36
def initialize():
    high = 65536
    low = -high
    for i in xrange(N):
        # random() generates a random float uniformly in the semi-open range [0.0, 1.0)
        individuals[i] = random.randint(low, high)
    print individuals

def evaluate():
    pass

# TODO: proof
def applyToMinimization(normFits):
    res = [0] * N
    for i in xrange(N):
        res[i] = (1 - normFits[i]) / (N - 1)
    return res

def getNormalizedFitnesses():
    fitnesses = [0] * N
    sum = 0
    for i in xrange(N):
        fitnesses[i] = fitness(individuals[i])
        sum += fitnesses[i]
    normFitnesses = [0] * N
    for i in xrange(N):
        normFitnesses[i] = fitnesses[i] / sum
    return applyToMinimization(normFitnesses)

def getChromIdx(cumProb, r):
    left = 0
    right = len(cumProb) - 1
    while left < right:
        middle = (left + right) / 2
        if cumProb[middle] < r:
            left = middle + 1
        else:
            right = middle
    return left

# @note Roulette-wheel selection
def runRWS():
    normFitnesses = getNormalizedFitnesses()
    print 'norm =', normFitnesses
    # NB: cumulativeProb[N - 1] can be != 1; I ignore this
    cumulativeProb = [0] * N
    cumulativeProb[0] = normFitnesses[0]
    for i in xrange(1, N):
        cumulativeProb[i] = cumulativeProb[i - 1] + normFitnesses[i]
    print 'cumul =', cumulativeProb
    newIndividuals = [0] * N
    for i in xrange(N):
        # NB: random() excludes upper bound 1.0; I ignore this
        newIndividuals[i] = getChromIdx(cumulativeProb, random.random())
    print newIndividuals
    return newIndividuals

def select():
    runRWS()

def applyOperators():
    pass

def stop():
    return False
