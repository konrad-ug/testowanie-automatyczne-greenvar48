from flask import Flask, request, jsonify
from .RejestrKont import RejestrKont
from .Konto import Konto

app = Flask(__name__)

@app.route('/konta/stworz_konto', methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    konto = Konto(dane['imie'], dane['nazwisko'], dane['pesel'])
    if RejestrKont.szukaj(dane['pesel']):
        return jsonify("Konto już istnieje"), 400
    else:
        RejestrKont.dodaj(konto)
        return jsonify("Konto stworzone"), 201

@app.route('/konta/ile_kont', methods=['GET'])
def ile_kont():
    return jsonify(ilosc = RejestrKont.ilosc()), 200

@app.route('/konta/konto/<pesel>', methods=['GET'])
def szukaj(pesel):
    rezultat = RejestrKont.szukaj(pesel)
    if rezultat is not None:
        return jsonify(
            imie=rezultat.imie,
            nazwisko=rezultat.nazwisko,
            pesel=rezultat.pesel,
            saldo=rezultat.saldo
        ), 200
    else:
        return jsonify("Nie znaleziono konta"), 404

@app.route('/konta/konto/<pesel>/update', methods=['PUT'])
def update(pesel):
    dane = request.get_json()
    rezultat = RejestrKont.szukaj(pesel)

    if rezultat is not None:
        for key in dane.keys():
            rezultat[key] = dane[key]
        return jsonify('Successfully updated field'), 200
    else:
        return jsonify('Failed to find account'), 404

@app.route('/konta/konto/<pesel>/delete', methods=['DELETE'])
def delete(pesel):
    rezultat = RejestrKont.szukaj(pesel)
    if rezultat is not None:
        RejestrKont.lista.pop(RejestrKont.lista.index(rezultat))
        return jsonify('Successfully deleted account'), 200
    else:
        return jsonify('Failed to find account'), 404
