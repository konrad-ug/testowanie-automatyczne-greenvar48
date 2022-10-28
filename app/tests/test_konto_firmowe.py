import unittest

from ..Konto import KontoFirmowe

class TestKontoFirmowe(unittest.TestCase):
    nazwa_firmy1 = "Sample Firma"
    nip1 = "1234567890"
    domyslne_saldo = 0

    def test_tworzenia_konta(self):
        konto = KontoFirmowe(self.nazwa_firmy1, self.nip1)
        self.assertEqual(konto.nazwa_firmy, self.nazwa_firmy1, "Nie zapisano nazwy")
        self.assertEqual(konto.nip, self.nip1, "Nie zapisano nipu!")

    def test_dlugosci_nipu(self):
        zly_nip = "213213"
        konto = KontoFirmowe(self.nazwa_firmy1, zly_nip);
        komunikat_o_zlym_nipie = "Niepoprawny NIP!"

        self.assertEqual(konto.nip, komunikat_o_zlym_nipie, "NIP ma niewłaściwą wartość!")
