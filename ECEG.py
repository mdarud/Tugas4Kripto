class ECEG:
    def genKey(pvk, ecpts):
        b = ecpts[0]
        pubk = [pvk * i for i in b]
        return b, pubk

    def encrypt(m, pts, b, pubk_o, k, mode='str'):
        if mode == 'bin':
            pms = [pts[int(b)] for b in m]
        else:
            pms = [pts[ord(c)] for c in m]
        kpb = [k * i for i in pubk_o]
        pc = ([k * i for i in b], [(pm[0] + kpb[0], pm[1] + kpb[1])
                                   for pm in pms])
        return pc

    def decrypt(pc, pvk, pts, mode='str'):
        kb = pc[0]
        bkb = [pvk * i for i in kb]
        pm = [(p[0] - bkb[0], p[1] - bkb[1]) for p in pc[1]]
        if mode == 'bin':
            m = [(pts.index(p)).to_bytes(1, 'big') for p in pm]
            o = b''
        else:
            m = [chr(pts.index(p)) for p in pm]
            o = ''
        return o.join(m)

    def save_ecpts(filename, ecpts):
        strpts = [str(pts[0]) + ',' + str(pts[1]) for pts in ecpts]
        strpts = ';'.join(strpts)
        f = open(filename, 'wt')
        f.write(strpts)
        f.close()

    def load_ecpts(filename):
        f = open(filename, 'rt')
        ecpts = f.read()
        ecpts = ecpts.split(';')
        def t_str_int(x): return (int(x[0]), int(x[1]))
        ecpts = [t_str_int(tuple(pts.split(','))) for pts in ecpts]
        return ecpts

    def save_public_key(filename, pubk):
        strpubk = ','.join([str(x) for x in pubk])
        f = open(filename, 'wt')
        f.write(strpubk)
        f.close()

    def save_private_key(filename, privk):
        f = open(filename, 'wt')
        f.write(str(privk))
        f.close()

    def load_public_key(filename):
        f = open(filename, 'rt')
        strpubk = f.read()
        return tuple([int(x) for x in strpubk.split(',')])

    def load_private_key(filename):
        f = open(filename, 'rt')
        pvk = f.read()
        return int(pvk)

    def save_output(filename, pc):
        strpc = []
        strpc.append(str(pc[0][0]) + ',' + str(pc[0][1]))
        ptspc = [str(pts[0]) + ',' + str(pts[1]) for pts in pc[1]]
        ptspc = ';'.join(ptspc)
        strpc.append(ptspc)
        strpc = '.'.join(strpc)
        f = open(filename, 'wt')
        f.write(strpc)
        f.close()

    def load_output(filename):
        def t_str_int(x): return (int(x[0]), int(x[1]))
        f = open(filename, 'rt')
        strpc = f.read()
        pc = strpc.split('.')
        pc[0] = t_str_int(pc[0].split(','))
        pc[1] = pc[1].split(';')
        pc[1] = [t_str_int(p.split(',')) for p in pc[1]]
        return pc
