import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
        
        if kod_rabatowy is not None and re.match("^PROMO_\S{3}$", kod_rabatowy):
            self.saldo = 50
        else:
            self.saldo = 0
