class RejestrKont:
    lista = []

    @classmethod
    def dodaj(cls, konto):
        cls.lista.append(konto)
    
    @classmethod
    def szukaj(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                return konto
                break
        return None

    @classmethod
    def ilosc(cls):
        return len(cls.lista)
    