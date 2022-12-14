import unittest
from parameterized import parameterized, parameterized_class

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

    @parameterized.expand([
        ([-25, -25, 100, 100, 100], 249, True),
        ([-25, -25, -100, 100, 100], 49, False),
        ([-25, -25, -100, 100, 100], 50, False),
        ([-50, 50, 50, 100], 149, False)
    ])

    def test_zaciagij_kredyt_osobiste(self, historia, kwota_kredytu, rezultat_zaciagnij):
        self.konto.historia = historia
        self.konto.saldo = sum(self.konto.historia)
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota_kredytu), rezultat_zaciagnij)
        if rezultat_zaciagnij:
            self.assertEqual(self.konto.saldo, sum(self.konto.historia) + kwota_kredytu)
