from paillier import Paillier
import utils
from ECEG import ECEG
from RSA import RSA
from elgamal import elgamal

m = 'Halo ini saya'
print('=====RSA=====')
e, d, n = RSA.genKey()
c = RSA.encrypt(m, e, n)
p = RSA.decrypt(c, d, n)
print(c)
print(p)

print('=====ElGamal=====')
y, x, g, p = elgamal.genKey()
c = elgamal.encrypt(m, y, g, p)
p = elgamal.decrypt(c, x, p)
print(c)
print(p)

m = 'Pesan yang akan dienkripsi dengan ECC harus dikonversi (encoding) menjadi titik di dalam kurva eliptik.'

print('=====PAILLIER=====')
_m = utils.str_to_int(m)

n, l, g, mu = Paillier.genKey(1024)
# print("PUBLIC KEY")
# print("({},{})".format(g, n))
# print("PRIVATE KEY")
# print("({},{})".format(l, mu))

print('Message')
print(m)

c = Paillier.encrypt(_m, g, n)
Paillier.save_output('output/pailier.out', c)

c = 0
c = Paillier.load_output('output/pailier.out')
p = Paillier.decrypt(c, l, mu, n)
print('Plaintext')
print(utils.int_to_str(p))
print()

print('=====ECEG=====')
pvk_a = utils.genPrime(1024)
pvk_b = utils.genPrime(1024)
p = utils.genPrime(8)
ecpts = utils.genECPoints(pvk_a, pvk_b, p, 5, 256)
b, pubk_a = ECEG.genKey(pvk_a, ecpts)
b, pubk_b = ECEG.genKey(pvk_b, ecpts)
k = p // 2

m = "Misalkan pesan M = 'ENCRYPT', yang dalam nilai ASCII adalah '69', '78', '67', '82', '89', '80', '84'. Setiap nilai ini dipetakan ke sebuah titik pada kurva eliptik"
print('Message')
print(m)

pc = ECEG.encrypt(m, ecpts, b, pubk_b, k)
ECEG.save_output('output/eceg.out', pc)

pc = ''
pc = ECEG.load_output('output/eceg.out')
pd = ECEG.decrypt(pc, pvk_b, ecpts)
print('Plaintext')
print(pd)
print()


print('=====PAILLIER FILE=====')
filepath = "input.txt"
f = open(filepath, 'rb').read()
_m = utils.bin_to_int(f)

n, l, g, mu = Paillier.genKey(1024)
Paillier.save_public_key('output/paillier.pub', g, n)
Paillier.save_private_key('output/paillier.pri', l, mu)

g, n = Paillier.load_public_key('output/paillier.pub')
l, mu = Paillier.load_private_key('output/paillier.pri')
# print("PUBLIC KEY")
# print("({},{})".format(g, n))
# print("PRIVATE KEY")
# print("({},{})".format(l, mu))

c = Paillier.encrypt(_m, g, n)
Paillier.save_output('output/pailier_file.out', c)

c = 0
c = Paillier.load_output('output/pailier_file.out')
p = Paillier.decrypt(c, l, mu, n)
filename = 'output/pailier_out.txt'
print('Output:', filename)
f = open(filename, 'wb')
f.write(utils.int_to_bin(p))
f.close()
print()

print('=====ECEG FILE=====')
filepath = "yoyo.gif"
f = open(filepath, 'rb').read()
m = f

pvk_a = utils.genPrime(1024)
pvk_b = utils.genPrime(1024)
p = utils.genPrime(8)
ecpts = utils.genECPoints(pvk_a, pvk_b, p, 0, 256)
b, pubk_a = ECEG.genKey(pvk_a, ecpts)
b, pubk_b = ECEG.genKey(pvk_b, ecpts)

ECEG.save_ecpts('output/ecpts.pub', ecpts)
ECEG.save_public_key('output/eceg_a.pub', pubk_a)
ECEG.save_public_key('output/eceg_b.pub', pubk_b)
ECEG.save_private_key('output/eceg_a.pri', pvk_a)
ECEG.save_private_key('output/eceg_b.pri', pvk_b)

k = p // 2

pubk_a = ''
pvk_a = ''
pubk_a = ECEG.load_public_key('output/eceg_a.pub')
pvk_a = ECEG.load_private_key('output/eceg_a.pri')
pc = ECEG.encrypt(m, ecpts, b, pubk_a, k, 'bin')
ECEG.save_output('output/eceg_a.out', pc)

pc = ''
pc = ECEG.load_output('output/eceg_a.out')
ecpts = ECEG.load_ecpts('output/ecpts.pub')
pd = ECEG.decrypt(pc, pvk_a, ecpts, 'bin')
filename = 'output/eceg_a_out.gif'
print('Output:', filename)
f = open(filename, 'wb')
f.write(pd)
f.close()

pubk_b = ''
pvk_b = ''
pubk_b = ECEG.load_public_key('output/eceg_b.pub')
pvk_b = ECEG.load_private_key('output/eceg_b.pri')
pc = ECEG.encrypt(m, ecpts, b, pubk_b, k, 'bin')
ECEG.save_output('output/eceg_b.out', pc)

pc = ''
pc = ECEG.load_output('output/eceg_b.out')
ecpts = ECEG.load_ecpts('output/ecpts.pub')
pd = ECEG.decrypt(pc, pvk_b, ecpts, 'bin')

filename = 'output/eceg_b_out.gif'
print('Output:', filename)
f = open(filename, 'wb')
f.write(pd)
f.close()
