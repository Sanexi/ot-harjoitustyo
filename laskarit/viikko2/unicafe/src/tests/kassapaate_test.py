import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_raha_alussa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisia_alussa(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaita_alussa(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_tarpeeksi_rahaa_kateinen_maukas1(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_tarpeeksi_rahaa_kateinen_maukas2(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_tarpeeksi_rahaa_kateinen_edullinen1(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)
        
    def test_tarpeeksi_rahaa_kateinen_edullinen2(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.edulliset, 1)
        

    def test_vahan_rahaa_kateinen_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100), 100)

    def test_vahan_rahaa_kateinen_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(100), 100)

    def test_tarpeeksi_rahaa_kortti_edullinen1(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 7.6")
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_tarpeeksi_rahaa_kortti_edullinen2(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_tarpeeksi_rahaa_kortti_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 6.0")
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

    def test_tarpeeksi_rahaa_kortti_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_vahan_rahaa_kortti_edullinen1(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.4")
        self.assertEqual(self.kassa.edulliset, 4)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)

    def test_vahan_rahaa_kortti_edullinen2(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_vahan_rahaa_kortti_maukas1(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
        self.assertEqual(self.kassa.maukkaat, 2)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)

    def test_vahan_rahaa_kortti_maukas2(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_saldo_muuttuu_kortin_kanssa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(str(self.kortti), "saldo: 20.0")
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kassan_saldo_muuttuu_kortin_kanssa_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)