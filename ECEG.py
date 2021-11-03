class ECEG:
    def genKey(pvk, ecpts):
        b = ecpts[0]
        pubk = [pvk * i for i in b]
        return b, pubk

    def encrypt(m, pts, b, pubk_o, k):
        pms = [pts[ord(c)] for c in m]
        kpb = [k * i for i in pubk_o]
        pc = ([k * i for i in b], [(pm[0] + kpb[0], pm[1] + kpb[1])
                                   for pm in pms])
        return pc

    def decrypt(pc, pvk, pts):
        kb = pc[0]
        bkb = [pvk * i for i in kb]
        pm = [(p[0] - bkb[0], p[1] - bkb[1]) for p in pc[1]]
        m = [chr(pts.index(p)) for p in pm]
        return "".join(m)
