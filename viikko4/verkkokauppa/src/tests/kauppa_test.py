import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 5)
            if tuote_id ==3:
                return Tuote(3, "Mars-jäätelö", 10)

        def varasto_palauta_varastoon(tuote_id):
            return tuote_id

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.varasto_mock.palauta_varastoon.side_effect = varasto_palauta_varastoon


        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreillä
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_tilisiirtoa_kutsutaan_oikeilla_parametreillä(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("liisa", "54321")

        # varmistetaan, että asiakas, tilinumero ja summa täsmäävät
        self.pankki_mock.tilisiirto.assert_called_with("liisa", ANY, "54321", ANY, 10)

    def test_yksi_tuotteista_on_loppunut(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("anna", "132435")

        self.pankki_mock.tilisiirto.assert_called_with("anna", ANY, "132435", ANY, 5)

    def test_edellinen_ostos_nollautuu(self):
        self.kauppa.aloita_asiointi()
        for _ in range(10):
            self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("heikki", "654321")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("heikki", "654321")

        self.pankki_mock.tilisiirto.assert_called_with("heikki", ANY, "654321", ANY, 5)

    def test_uusi_tapahtuma_saa_uuden_viitenumeron(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("marju", "1234567")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 42, ANY, ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("jukka", "2345678")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 43, ANY, ANY, ANY)
        
    def test_ostoskorin_tyhjennys(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        
        self.assertEqual(self.varasto_mock.saldo(1), 10)

        



