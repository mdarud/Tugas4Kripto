import utils
import random


class Paillier:
    def genKey(length=2048):
        while True:
            p = utils.genPrime(length)
            q = utils.genPrime(length)
            if utils.gcd(p*q, (p-1)*(q-1)) == 1:
                break
        n = p * q
        l = utils.lcm(p-1, q-1)
        g = n + 1
        def L(x): return (x - 1)//n
        z = L(pow(g, l, n*n))
        mu = pow(z, -1, n)
        return n, l, g, mu

    def encrypt(m, g, n):
        while True:
            r = random.randint(0, n - 1)
            if utils.gcd(r, n) == 1:
                break
        n2 = pow(n, 2)
        return (((n * m + 1) % n2) * pow(r, n, n2)) % n2
        # return (pow(g, m) * pow(r, n)) % pow(n, 2)

    def decrypt(c, l, mu, n):
        def L(x): return (x - 1)//n
        return (L(pow(c, l, n*n)) * mu) % n

    def save_public_key(filename, g, n):
        f = open(filename, 'wt')
        f.write(str(g) + ',' + str(n))
        f.close()

    def save_private_key(filename, l, mu):
        f = open(filename, 'wt')
        f.write(str(l) + ',' + str(mu))
        f.close()

    def load_public_key(filename):
        f = open(filename, 'r')
        g, n = f.read().split(',')
        return int(g), int(n)

    def load_private_key(filename):
        f = open(filename, 'r')
        l, mu = f.read().split(',')
        return int(l), int(mu)

    def save_output(filename, c):
        f = open(filename, 'wt')
        f.write(str(c))
        f.close()

    def load_output(filename):
        f = open(filename, 'rt')
        c = f.read()
        return int(c)
