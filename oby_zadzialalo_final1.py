import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        f = open('taski.json')
        wynik = json.loads(f)
        return wynik
        # TODO odczytaj plik i zdekoduj treść tutaj
        pass

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        f = open('taski.json')
        wynik = json.loads(f)
        return wynik
        pass
