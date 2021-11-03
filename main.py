from paillier import Paillier
import utils
from ECEG import ECEG

m = 'Pesan yang akan dienkripsi dengan ECC harus dikonversi (encoding) menjadi titik di dalam kurva eliptik.'

print('=====PAILLIER=====')
_m = utils.str_to_int(m)
print(_m)

n, l, g, mu = Paillier.genKey(1024)
print("PUBLIC KEY")
print("({},{})".format(g, n))
print("PRIVATE KEY")
print("({},{})".format(l, mu))

print('Message')
print(m)

c = Paillier.encrypt(_m, g, n)
print('Ciphertext')
print(c)

p = Paillier.decrypt(c, l, mu, n)
print('Plaintext')
print(utils.int_to_str(p))
print()

print('=====ECEG=====')
pvk_a = utils.genPrime(1024)
pvk_b = utils.genPrime(1024)
p = utils.genPrime(8)
ecpts = utils.genECPoints(pvk_a, pvk_b, p, 0, 255)
b, pubk_a = ECEG.genKey(pvk_a, ecpts)
b, pubk_b = ECEG.genKey(pvk_b, ecpts)
k = p // 2
print(len(ecpts))

m = "Misalkan pesan M = 'ENCRYPT', yang dalam nilai ASCII adalah '69', '78', '67', '82', '89', '80', '84'. Setiap nilai ini dipetakan ke sebuah titik pada kurva eliptik"
print('Message')
print(m)

pc = ECEG.encrypt(m, ecpts, b, pubk_b, k)
print('CipherPoints')
print(pc)

pd = ECEG.decrypt(pc, pvk_b, ecpts)
print('Plaintext')
print(pd)
