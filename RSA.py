import utils

class RSA:
    def genKey():
        p = 0
        q = 0
        while (p == q):
            p = utils.genPrimeRange(100, 500)
            q = utils.genPrimeRange(100, 500)
        n = p * q
        totient = (p - 1) * (q - 1)
        e = utils.genE(totient)
        d = utils.multi_inverse(e, totient)

        return e, d, n

    def encrypt(plaintext, e, n, block_length=2):
        encrypted_blocks = []
        block = ord(plaintext[0])
        for i in range(1, len(plaintext)):
            if (i % (block_length) == 0):
                encrypted_blocks.append(block)
                block = 0
            block = block * pow(10, block_length+1) + ord(plaintext[i])
        encrypted_blocks.append(block)
        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str(pow(encrypted_blocks[i], e, n))
        ciphertext = " ".join(encrypted_blocks)

        return ciphertext

    def decrypt(ciphertext, d, n, block_length=2):
        blocks = ciphertext.split(' ')
        _blocks = []
        for b in blocks:
            _blocks.append(int(b))
        plaintext = ""
        for i in range(len(_blocks)):
            _blocks[i] = pow(_blocks[i], d, n)
            temp = ""
            for j in range(block_length):
                temp = chr(_blocks[i] % pow(10, block_length+1)) + temp
                _blocks[i] //= pow(10, block_length+1)
            plaintext += temp

        return plaintext
