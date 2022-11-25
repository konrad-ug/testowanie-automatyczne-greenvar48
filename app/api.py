from flask import Flask, request, jsonify
from .RejestrKont import RejestrKont
from .Konto import Konto

app = Flask(__name__)

@app.route('/konta/stworz_konto', methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    konto = Konto(dane['imie'], dane['nazwisko'], dane['pesel'])
    RejestrKont.dodaj(konto)
    return jsonify("Konto stworzone"), 201

@app.route('/konta/ile_kont', methods=['GET'])
def ile_kont():
    return jsonify(ilosc= RejestrKont.ilosc()), 200

@app.route('/konta/konto/<pesel>', methods=['GET'])
def szukaj(pesel):
    rezultat = RejestrKont.szukaj(pesel)
    if rezultat is not None:
        return jsonify(
            imie=rezultat.imie,
            nazwisko=rezultat.nazwisko,
            pesel=rezultat.pesel
        ), 200
    else:
        return jsonify("Nie znaleziono konta"), 404
