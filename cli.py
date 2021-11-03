from paillier import Paillier
import utils
from ECEG import ECEG
from RSA import RSA
from elgamal import elgamal

exit = False
while not(exit):
    print("Menu:")
    print("1. RSA")
    print("2. ElGamal")
    print("3. Paillier")
    print("4. ECEG")
    print("0. Exit")
    opt = int(input("Silakan pilih nomor pada menu: "))

    if opt == 1:
        print("RSA:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Generate Key")
        print("0. Exit")
        _opt = int(input("Silakan pilih nomor pada menu: "))
        if _opt == 1:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                m = str(input("Masukkan pesan untuk dienkripsi: "))
                k = str(input("Masukkan nama file kunci public: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                e = int(key_string[0])
                n = int(key_string[1])
                c = RSA.encrypt(m, e, n)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f.open("EncryptedRSA.txt", "w")
                    f.write(c)
                    f.close()
            elif tipe == 2:
                m = str(input("Masukkan nama file untuk dienkripsi: "))
                f = open(m, 'r')
                txt = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci public: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                e = int(key_string[0])
                n = int(key_string[1])
                c = RSA.encrypt(txt, e, n)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("EncryptedRSA.txt", "w")
                    f.write(c)
                    f.close()
        elif _opt == 2:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                d = int(key_string[0])
                n = int(key_string[1])
                m = RSA.decrypt(c, d, n)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedRSA.txt", "w")
                    f.write(m)
                    f.close()
            elif tipe == 2:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                f = open(c, 'r')
                cip = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                d = int(key_string[0])
                n = int(key_string[1])
                m = RSA.decrypt(cip, d, n)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedRSA.txt", "w")
                    f.write(m)
                    f.close()
            elif _opt == 3:
                e, d, n = RSA.genKey()
                name = str(input("Nama files kunci: "))
                f = open(name + ".pub", "w")
                f.write(str(e) + ", " + str(n))
                f.close()
                f = open(name + ".pri", "w")
                f.write(str(d) + ", " + str(n))
                f.close()
            else:
                exit = True
    elif opt == 2:
        print("ElGamal:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Generate Key")
        print("0. Exit")
        _opt = int(input("Silakan pilih nomor pada menu: "))
        if _opt == 1:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                m = str(input("Masukkan pesan untuk dienkripsi: "))
                k = str(input("Masukkan nama file kunci public: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                y, g, p = [int(x) for x in key.split(', ')]
                c = elgamal.encrypt(m, y, g, p)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f.open("EncryptedElGamal.txt", "w")
                    f.write(c)
                    f.close()
            elif tipe == 2:
                m = str(input("Masukkan nama file untuk dienkripsi: "))
                f = open(m, 'r')
                txt = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci public: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                y, g, p = [int(x) for x in key.split(', ')]
                c = elgamal.encrypt(txt, y, g, p)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("EncryptedElGamal.txt", "w")
                    f.write(c)
                    f.close()
        elif _opt == 2:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                x, p = [int(x) for x in key.split(', ')]
                m = elgamal.decrypt(c, x, p)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedElGamal.txt", "w")
                    f.write(m)
                    f.close()
            elif tipe == 2:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                f = open(c, 'r')
                cip = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                x, p = [int(x) for x in key.split(', ')]
                m = elgamal.decrypt(cip, x, p)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedElGamal.txt", "w")
                    f.write(m)
                    f.close()
            elif _opt == 3:
                y, x, g, p = elgamal.genKey()
                name = str(input("Nama files kunci: "))
                f = open(name + ".pub", "w")
                f.write(str(y) + ", " + str(g) + ", " + str(p))
                f.close()
                f = open(name + ".pri", "w")
                f.write(str(x) + ", " + str(p))
                f.close()
            else:
                exit = True
    elif opt == 3:
        print("Paillier:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Generate Key")
        print("0. Exit")
        _opt = int(input("Silakan pilih nomor pada menu: "))
        if _opt == 1:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                m = str(input("Masukkan pesan untuk dienkripsi: "))
                k = str(input("Masukkan nama file kunci public: "))
                _m = utils.str_to_int(m)
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                g = int(key_string[0])
                n = int(key_string[1])
                c = Paillier.encrypt(_m, g, n)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f.open("EncryptedPaillier.txt", "w")
                    f.write(c)
                    f.close()
            elif tipe == 2:
                m = str(input("Masukkan nama file untuk dienkripsi: "))
                f = open(m, 'r')
                txt = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci public: "))
                _m = utils.str_to_int(txt)
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                g = int(key_string[0])
                n = int(key_string[1])
                c = Paillier.encrypt(_m, g, n)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("EncryptedPaillier.txt", "w")
                    f.write(c)
                    f.close()
        elif _opt == 2:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                l, mu, n = [int(x) for x in key.split(', ')]
                m = Paillier.decrypt(c, l, mu, n)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedPaillier.txt", "w")
                    f.write(m)
                    f.close()
            elif tipe == 2:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                f = open(c, 'r')
                cip = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                l, mu, n = [int(x) for x in key.split(', ')]
                m = Paillier.decrypt(cip, l, mu, n)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedPaillier.txt", "w")
                    f.write(m)
                    f.close()
            elif _opt == 3:
                n, l, g, mu = Paillier.genKey(1024)
                name = str(input("Nama files kunci: "))
                f = open(name + ".pub", "w")
                f.write(str(g) + ", " + str(n))
                f.close()
                f = open(name + ".pri", "w")
                f.write(str(l) + ", " + str(mu))
                f.close()
            else:
                exit = True
    elif opt == 4:
        print("ECEG:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Generate Key")
        print("0. Exit")
        _opt = int(input("Silakan pilih nomor pada menu: "))
        if _opt == 1:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                m = str(input("Masukkan pesan untuk dienkripsi: "))
                k = str(input("Masukkan nama file kunci public: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                g = int(key_string[0])
                n = int(key_string[1])
                c = Paillier.encrypt(m, ecpts, b, pubk_a, k, str)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f.open("EncryptedECEG.txt", "w")
                    f.write(c)
                    f.close()
            elif tipe == 2:
                m = str(input("Masukkan nama file untuk dienkripsi: "))
                f = open(m, 'r')
                txt = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci public: "))
                _m = utils.str_to_int(txt)
                f = open(k, 'r')
                key = f.read()
                f.close()
                key_string = key.split(", ")
                g = int(key_string[0])
                n = int(key_string[1])
                c = Paillier.encrypt(_m, g, n)
                print("Ciphertext: {}".format(c))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("EncryptedECEG.txt", "w")
                    f.write(c)
                    f.close()
        elif _opt == 2:
            tipe = int(input("1. Text/ 2. File? "))
            if tipe == 1:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                l, mu, n = [int(x) for x in key.split(', ')]
                m = Paillier.decrypt(c, l, mu, n)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedECEG.txt", "w")
                    f.write(m)
                    f.close()
            elif tipe == 2:
                c = str(input("Masukkan pesan untuk didekripsi: "))
                f = open(c, 'r')
                cip = f.read()
                f.close()
                k = str(input("Masukkan nama file kunci private: "))
                f = open(k, 'r')
                key = f.read()
                f.close()
                l, mu, n = [int(x) for x in key.split(', ')]
                m = Paillier.decrypt(cip, l, mu, n)
                print("Plaintext: {}".format(m))
                sv = str(input("Save pada file (y/n)? ")).lower()
                if sv == "y":
                    f = open("DecryptedECEG.txt", "w")
                    f.write(m)
                    f.close()
            elif _opt == 3:
                n, l, g, mu = Paillier.genKey(1024)
                name = str(input("Nama files kunci: "))
                f = open(name + ".pub", "w")
                f.write(str(g) + ", " + str(n))
                f.close()
                f = open(name + ".pri", "w")
                f.write(str(l) + ", " + str(mu))
                f.close()
            else:
                exit = True
    else:
        exit = True
