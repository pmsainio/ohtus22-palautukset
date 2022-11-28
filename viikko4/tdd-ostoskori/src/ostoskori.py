from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        määrä = 0
        for ostos in self.kori:
            määrä += ostos.lukumaara()
        return määrä
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.kori:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        for item in self.kori:
            if ostos.tuotteen_nimi() == item.tuotteen_nimi():
                item.muuta_lukumaaraa(1)
                return
        self.kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        ostos = Ostos(poistettava)
        for item in self.kori:
            if ostos.tuotteen_nimi() == item.tuotteen_nimi():
                item.muuta_lukumaaraa(-1)
                if item.lukumaara() == 0:
                    self.kori.remove(item)
                return



    def tyhjenna(self):
        self.kori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
