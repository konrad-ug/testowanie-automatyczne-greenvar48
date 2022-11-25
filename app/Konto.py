import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.oplata_za_ekspresowy = 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.historia = []

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
        
        if kod_rabatowy is not None \
            and re.match("^PROMO_\S{3}$", kod_rabatowy) \
            and int(self.pesel[2:4]) < 81 \
            and (int(self.pesel[2:4]) > 12 or int(self.pesel[0:2]) > 60):
            self.saldo = 50
        else:
            self.saldo = 0
        
    def przelew_wychodzacy(self, kwota):
        if self.saldo - kwota >= 0:
            self.saldo -= kwota
            self.historia.append(- kwota)

    def przelew_przychodzący(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def przelew_ekspresowy(self, kwota):
        if self.saldo - kwota >= 0:
            self.saldo -= kwota + self.oplata_za_ekspresowy
            self.historia.append(- self.oplata_za_ekspresowy)
            self.historia.append(- kwota)

    def zaciagnij_kredyt(self, kwota):
        if len(self.historia) > 4 \
        and all(transakcja > 0 for transakcja in self.historia[-1:-4:-1]) \
        and sum(self.historia[-1:-6:-1]) > kwota:
            self.saldo += kwota;
            return True;
        else:
            return False;
            

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.oplata_za_ekspresowy = 5
        self.nazwa_firmy = nazwa_firmy
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip
        
        self.saldo = 0
        self.historia = []

    def zaciagnij_kredyt(self, kwota):
        if self.saldo >= 2 * kwota and \
        any(przelew == -1775 for przelew in self.historia):
            self.saldo += kwota
            return True
        else:
            return False
        

