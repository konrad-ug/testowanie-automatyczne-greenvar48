import unittest
import requests
from parameterized import parameterized, parameterized_class

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestApiAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        RejestrKont.lista = []
    
    imie1 = "Jan"
    nazwisko1 = "Kowalski"
    pesel1 ="01234567891"

    @parameterized.expand([
        (imie1, nazwisko1, pesel1, 201),
        (imie1, nazwisko1, pesel1, 400)
    ])

    def test_1_stworz_konto(self, imie, nazwisko, pesel, exp_response):
        response = requests.post('http://127.0.0.1:5000/konta/stworz_konto', json={
            "imie": imie,
            "nazwisko": nazwisko,
            "pesel": pesel})
        
        self.assertEqual(response.status_code, exp_response)
        
    @parameterized.expand([
        (pesel1, {'imie': imie1, 'nazwisko': nazwisko1, 'pesel': pesel1, 'saldo': 0}, 200),
        ('11111111111', "Nie znaleziono konta", 404)
    ])

    def test_2_znajdz_konto(self, pesel, exp_content, exp_response):
        response = requests.get(f"http://127.0.0.1:5000/konta/konto/{pesel}")
        
        self.assertEqual(response.status_code, exp_response)
        self.assertEqual(response.json(), exp_content)
    
    def test_3_ile_kont(self):
        response = requests.get(f"http://127.0.0.1:5000/konta/ile_kont")

        self.assertEqual(response.json()['ilosc'], 1, 'Niepoprawna ilość kont!')

    @parameterized.expand([
        (pesel1, {'saldo': 1000}, 'Successfully updated field', 200),
        ('00000000000', {'saldo': 1000}, 'Failed to find account', 404),
    ])

    def test_4_update_konta(self, pesel, body, exp_content, exp_response):
        response = requests.put(f"http://127.0.0.1:5000/konta/konto/{pesel}/update", json=body)
        
        self.assertEqual(response.status_code, exp_response)
        self.assertEqual(response.json(), exp_content)

    @parameterized.expand([
        (pesel1, 'Successfully deleted account', 200),
        ('00000000000', 'Failed to find account', 404),
    ])

    def test_5_usuwanie_konta(self, pesel, exp_content, exp_response):
        response = requests.delete(f"http://127.0.0.1:5000/konta/konto/{pesel}/delete")
        
        self.assertEqual(response.status_code, exp_response)
        self.assertEqual(response.json(), exp_content)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []
    