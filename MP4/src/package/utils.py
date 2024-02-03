import string
import random


def idNumGenerator(size = 10, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def idGenerator(size = 10, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
