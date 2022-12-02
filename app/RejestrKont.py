class RejestrKont:
    lista = []

    @classmethod
    def dodaj(cls, konto):
        cls.lista.append(konto)
    
    @classmethod
    def szukaj(cls, pesel):
        for konto in cls.lista:
            print(konto.pesel)
            print(pesel)
            print()
            if konto.pesel == pesel:
                return konto
        return None

    @classmethod
    def ilosc(cls):
        return len(cls.lista)
    