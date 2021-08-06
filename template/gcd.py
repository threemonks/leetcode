"""
Greatest common denomenator

"""
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x