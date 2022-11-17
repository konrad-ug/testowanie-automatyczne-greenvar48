import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe

class TestksiegowanieOperacji(unittest.TestCase):
    imie1 = "Dariusz"
    nazwisko1 = "Januszewski"
    pesel1 = "01234567891"
    domyslne_saldo = 0

    nazwa_firmy1 = "Najlepsza Firma"
    nip1 = "0123456789"

    oplata_osobiste = 1
    oplata_firmowe = 5

    def test_przelewu_wychodzacego_osobiste(self):
        konto = Konto(self.imie1, self.nazwisko1, self.pesel1)
        pierwotne_saldo = 500
        konto.saldo = pierwotne_saldo
        kwota_przelewu = 100
        konto.przelew_wychodzacy(kwota_przelewu)
        self.assertEqual(konto.saldo, pierwotne_saldo - kwota_przelewu, "Saldo ma niepoprawną wartość!")

        pierwotne_saldo = 0
        konto.saldo = pierwotne_saldo
        kwota_przelewu = 100
        konto.przelew_wychodzacy(kwota_przelewu)
        self.assertEqual(konto.saldo, pierwotne_saldo, "Saldo ma niepoprawną wartość!")

    def test_przelewu_wychodzacego_firmowe(self):
        konto = KontoFirmowe(self.nazwa_firmy1, self.nip1)
        pierwotne_saldo = 500
        konto.saldo = pierwotne_saldo
        kwota_przelewu = 100
        konto.przelew_wychodzacy(kwota_przelewu)
        self.assertEqual(konto.saldo, pierwotne_saldo - kwota_przelewu, "Saldo ma niepoprawną wartość!")

        pierwotne_saldo = 0
        konto.saldo = pierwotne_saldo
        kwota_przelewu = 100
        konto.przelew_wychodzacy(kwota_przelewu)
        self.assertEqual(konto.saldo, pierwotne_saldo, "Saldo ma niepoprawną wartość!")
    
    def test_przelewu_przychodzącego_osobiste(self):
        konto = Konto(self.imie1, self.nazwisko1, self.pesel1)
        pierwotne_saldo = 500
        konto.saldo = pierwotne_saldo
        kwota_przelewu = 100
        konto.przelew_przychodzący(kwota_przelewu)
        self.assertEqual(konto.saldo, pierwotne_saldo + kwota_przelewu, "Saldo ma niepoprawną wartość!")
    
    def test_przelewu_przychodzącego_firmowe(self):
        konto = KontoFirmowe(self.nazwa_firmy1, self.nip1)
        pierwotne_saldo = 500
        konto.saldo = pierwotne_saldo
        kwota_przelewu = 100
        konto.przelew_przychodzący(kwota_przelewu)
        self.assertEqual(konto.saldo, pierwotne_saldo + kwota_przelewu, "Saldo ma niepoprawną wartość!")
    
    def test_przelewu_ekspresowego_konta_osobiste(self):
        konto = Konto(self.imie1, self.nazwisko1, self.pesel1)
        pierwotne_saldo = 500
        konto.saldo = pierwotne_saldo
        kwota = 100
        
        konto.przelew_ekspresowy(kwota)
        self.assertEqual(konto.saldo, pierwotne_saldo - kwota - self.oplata_osobiste, "Niepoprawne saldo przy przelewie ekspresowym!")

    def test_przelewu_ekspresowego_konta_firmowe(self):
        konto = KontoFirmowe(self.nazwa_firmy1, self.nip1)
        pierwotne_saldo = 500
        konto.saldo = pierwotne_saldo
        kwota = 100
        
        konto.przelew_ekspresowy(kwota)
        self.assertEqual(konto.saldo, pierwotne_saldo - kwota - self.oplata_firmowe, "Niepoprawne saldo przy przelewie ekspresowym!")

    def test_historii_przelewów_personalne(self):
        konto = Konto(self.imie1, self.nazwisko1, self.pesel1)
        kwoty = [500, 100, 300]
        konto.saldo = 1000
        konto.przelew_wychodzacy(kwoty[0])
        konto.przelew_przychodzący(kwoty[1])
        konto.przelew_ekspresowy(kwoty[2])
        self.assertEqual(konto.historia, [-kwoty[0], kwoty[1], -self.oplata_osobiste, -kwoty[2]], 
        "Niepoprawnie zapisana historia!")
    
    def test_historii_przelewów_firmowe(self):
        konto = KontoFirmowe(self.nazwa_firmy1, self.nip1)
        kwoty = [500, 100, 300]
        konto.saldo = 1000
        konto.przelew_wychodzacy(kwoty[0])
        konto.przelew_przychodzący(kwoty[1])
        konto.przelew_ekspresowy(kwoty[2])
        self.assertEqual(konto.historia, [-kwoty[0], kwoty[1], -self.oplata_firmowe, -kwoty[2]], 
        "Niepoprawnie zapisana historia!")