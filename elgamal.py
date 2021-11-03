import utils
import random


class elgamal:
    def genKey():
        p = utils.genPrimeRange(300000, 400000)
        g = random.randint(2, p - 1)
        x = random.randint(1, p - 2)
        y = pow(g, x, p)
        return y, x, g, p

    def encrypt(plaintext, y, g, p, block_length=2):
        blocks = []
        block = ord(plaintext[0]) if len(plaintext) > 0 else -1
        if len(plaintext) % block_length:
            plaintext += chr(0)
        for i in range(1, len(plaintext)):
            if (i % block_length == 0):
                blocks.append(block)
                block = 0
            block = block * pow(10, block_length+1) + ord(plaintext[i])
        blocks.append(block)
        k = random.randint(1, p - 2)
        for i in range(len(blocks)):
            blocks[i] = (pow(g, k, p), (pow(y, k, p) * blocks[i]) % p)
        ciphertext = ' '.join([str(item) for pair in blocks for item in pair])

        return ciphertext

    def decrypt(ciphertext, x, p, block_length=2):
        block = ciphertext.split(' ')
        blocks = []
        for i in range(0, len(block), 2):
            blocks.append((int(block[i]), int(block[i + 1])))
        plaintext = ''
        for a, b in blocks:
            a_x_inverse = pow(a, p - 1 - x, p)
            plain = (b * a_x_inverse) % p
            temp = ''
            for _ in range(block_length):
                temp = chr(plain % pow(10, block_length+1)) + temp
                plain //= pow(10, block_length+1)
            plaintext += temp

        return plaintext
