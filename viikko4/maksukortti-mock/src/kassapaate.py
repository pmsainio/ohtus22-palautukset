from maksukortti import Maksukortti

HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti:Maksukortti, summa):
        if summa == abs(summa):
            kortti.lataa(summa)
        pass

    def osta_lounas(self, kortti:Maksukortti):
        if kortti.saldo > HINTA:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
        pass
