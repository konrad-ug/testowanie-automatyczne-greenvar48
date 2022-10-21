import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie1 = "Dariusz"
        nazwisko1 = "Januszewski"
        pesel1 = "01234567891"
        domyslne_saldo = 0

        pierwsze_konto = Konto(imie1, nazwisko1, pesel1)
        self.assertEqual(pierwsze_konto.imie, imie1, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko1, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, domyslne_saldo, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel1, "PESEL nie został zapisany!")

        zly_pesel = "11111"
        konto_zly_pesel = Konto(imie1, nazwisko1, zly_pesel)
        self.assertEqual(konto_zly_pesel.pesel, "Niepoprawny pesel!", "Długość numeru PESEL nie jest sprawdzana!")

        rabat_saldo = 50
        kod_rabatowy1 = "PROMO_G4d"
        zly_kod_rabatowy ="PROMO_gg"
        konto_z_rabatem = Konto(imie1, nazwisko1, pesel1, kod_rabatowy1)
        self.assertEqual(konto_z_rabatem.saldo, rabat_saldo, "Nie dodano 50 zl do konta z rabatem!")

        konto_ze_zlym_rabatem = Konto(imie1, nazwisko1, pesel1, zly_kod_rabatowy)
        self.assertEqual(konto_ze_zlym_rabatem.saldo, domyslne_saldo, "Rabat jest naliczany za niepoprawny kod!")
        