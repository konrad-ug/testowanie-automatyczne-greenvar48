import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie1 = "Dariusz"
    nazwisko1 = "Januszewski"
    pesel1 = "01234567891"
    domyslne_saldo = 0
    rabat_saldo = 50
    kod_rabatowy1 = "PROMO_G4d"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie1, self.nazwisko1, self.pesel1)
        self.assertEqual(pierwsze_konto.imie, self.imie1, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko1, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, self.domyslne_saldo, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel1, "PESEL nie został zapisany!")

    def test_poprawnosci_peselu(self):
        zly_pesel = "11111"
        konto_zly_pesel = Konto(self.imie1, self.nazwisko1, zly_pesel)
        self.assertEqual(konto_zly_pesel.pesel, "Niepoprawny pesel!", "Długość numeru PESEL nie jest sprawdzana!")

    def test_poprawnosci_kodu_rabatowego(self):
        zly_kod_rabatowy ="PROMO_gg"
        konto_z_rabatem = Konto(self.imie1, self.nazwisko1, self.pesel1, self.kod_rabatowy1)
        self.assertEqual(konto_z_rabatem.saldo, self.rabat_saldo, "Nie dodano 50 zl do konta z rabatem!")

        konto_ze_zlym_rabatem = Konto(self.imie1, self.nazwisko1, self.pesel1, zly_kod_rabatowy)
        self.assertEqual(konto_ze_zlym_rabatem.saldo, self.domyslne_saldo, "Rabat jest naliczany za niepoprawny kod!")

    def test_wieku_pod_rabat(self):
        pesel_za_stary = "60011513574"
        konto_z_za_starym_peselem = Konto(self.imie1, self.nazwisko1, pesel_za_stary, self.kod_rabatowy1);
        self.assertEqual(konto_z_za_starym_peselem.saldo, self.domyslne_saldo, "Naliczono rabat osobie za starej!")
