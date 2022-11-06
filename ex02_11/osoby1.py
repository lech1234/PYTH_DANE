"""
Skrypt tworzy listę słowników opisujących osoby, a następnie wykonuje operacje na tych danych.
"""

# Dane wejściowe
osoba1 = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'adres': 'Warszawa',
    'plec': True,
    'wiek': 22
}
osoba2 = {
    'imie': 'Anna',
    'nazwisko': 'Jabłońska',
    'adres': 'Poznań',
    'plec': False,
    'wiek': 18
}
osoba3 = {
    'imie': 'Tomasz',
    'nazwisko': 'Nowak',
    'adres': 'Wrocław',
    'plec': True,
    'wiek': 30
}
osoba4 = {
    'imie': 'Alicja',
    'nazwisko': 'Młynarska',
    'adres': 'Warszawa',
    'plec': False,
    'wiek': 25
}

lista_osob = [osoba1, osoba2, osoba3, osoba4]

# lista mężczyzn mieszkających w Warszawie
warszawiacy = [osoba for osoba in lista_osob if osoba['plec'] and osoba['adres'] == 'Warszawa']
print('1. Lista warszawiaków:', *warszawiacy, sep='\n', end='\n\n')

# lista dwudziestolatków
dwudziestoletni = [osoba for osoba in lista_osob if 20 <= osoba['wiek'] < 30]
print('2. Lista dwudziestolatków i dwudziestolatek:', *dwudziestoletni, sep='\n', end='\n\n')

# średnia wieku kobiet o imionach rozpoczynających się na 'A'
lista_wieku_kobiet_na_A = [osoba['wiek'] for osoba in lista_osob if not osoba['plec'] and osoba['imie'].startswith('A')]
# zamiast:
#    osoba['imie'].startswith('A')
# można też napisać:
#    osoba['imie'][0] == 'A'

srednia_wieku = sum(lista_wieku_kobiet_na_A) / len(lista_wieku_kobiet_na_A)
print('3. Średnia wieku kobiet o imionach na A...:', srednia_wieku)

# w ostatnim przykładzie do wyliczenia średniej można także użyć funkcji mean z pakietu statistics
# import statistics
# print('Średnia wieku kobiet o imionach na A...:', statistics.mean(lista_wieku_kobiet_na_A))
