import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe

class TestKredyty(unittest.TestCase):
    imie1 = "Dariusz"
    nazwisko1 = "Januszewski"
    pesel1 = "01234567891"
    domyslne_saldo = 0

    nazwa_firmy1 = "Najlepsza Firma"
    nip1 = "0123456789"

    oplata_osobiste = 1
    oplata_firmowe = 5

    def setUp(self):
        self.konto = Konto(self.imie1, self.nazwisko1, self.pesel1)

    def test_zaciagij_kredyt_osobiste_spelnione_warunki(self):
        kwoty = [-25, -25, 100, 100, 100]
        self.konto.historia = kwoty
        self.konto.saldo = sum(self.konto.historia)
        kwota_kredytu = 249
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota_kredytu), True, "Kredyt powinien zostać udzielony!")
        self.assertEqual(self.konto.saldo, sum(self.konto.historia) + kwota_kredytu, "Saldo konta nie zgadza się po udzieleniu kredytu!")

    def test_zaciagij_kredyt_osobiste_zla_ilosc_wplywow(self):
        kwoty = [-25, -25, -100, 100, 100]
        self.konto.historia = kwoty
        self.konto.saldo = sum(self.konto.historia)
        kwota_kredytu = 49
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota_kredytu), False, "Ostatnie 3 transakcje nie sią wpływami!")

    def test_zaciagij_kredyt_osobiste_za_male_saldo_5_transakcji(self):
        kwoty = [-25, -25, -100, 100, 100]
        self.konto.historia = kwoty
        self.konto.saldo = sum(self.konto.historia)
        kwota_kredytu = 50
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota_kredytu), False, "Saldo ostatnich 5 transakcji nie jest większe od kwoty kredytu!")

    def test_zaciagij_kredyt_osobiste_mniej_niz_5_transakcji(self):
        kwoty = [-25, -25, 100, 100]
        self.konto.historia = kwoty
        self.konto.saldo = sum(self.konto.historia)
        kwota_kredytu = 149
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota_kredytu), False, "Konto wykonało mniej niż 5 transakcji!")
