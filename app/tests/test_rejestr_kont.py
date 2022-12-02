import unittest
from parameterized import parameterized, parameterized_class

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        RejestrKont.lista = [
            Konto('Darek', 'Kowalski', '01234567891'),
            Konto('Marek', 'Król', '81103194199'),
            Konto('Franek', 'Tran', '78121651858'),
            Konto('Hubert', 'Śliwa', '57060194459')
        ]
    
    def test_dodawania_konta_personalnego(self):
        pesel ='54012124573'
        konto = Konto('Tadeusz', 'Tarnecki', pesel)
        RejestrKont.dodaj(konto)
        self.assertEqual(RejestrKont.lista[4], konto, 'Konto nie zostało zapisane!')
        self.assertEqual(RejestrKont.szukaj('54012124573'), konto, "Nie znaleziono konta, które dodano!")

    def test_szukanie_nieistniejacego_konta(self):
        self.assertEqual(RejestrKont.szukaj('00000000000'), None, 'Znaleziono konto, które nie istnieje!')
    
    def test_ilosc_kont(self):
        self.assertEqual(RejestrKont.ilosc(), 5, "Zwrócona ilość kont nie zgadza się!")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []
