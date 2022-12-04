import random
import time

def randinteger(min, max):
    return random.randint(min, max)

def randfloat(min, max):
    return random.uniform(min, max)

def randbytes(amount):
    return random.randbytes(amount)

def rand():
    return random.Random()

def randeven(min, max):
    num = 1
    while (num % 2) != 0:
        num = random.randint(min, max)
    return num

def randodd(min, max):
    num = 0
    while (num % 2) == 0:
        num = random.randint(min, max)
    return num

def randitem(deck):
    return random.choice(deck)

def randletter():
    return random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j" "k", "l", "z", "x", "c", "v", "b", "n", "m"])

def randduplicate(what, min, max):
    return str(what) * random.randint(min, max)

def randrgb():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def randwait(min, max):
    time.sleep(random.randint(min, max))

def randshuffle(deck):
    return random.shuffle(deck)
