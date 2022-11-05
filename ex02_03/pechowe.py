"""
Skrypt oblicza ile w danym roku jest piątków 13-tego.

Do obliczeń wykorzystywany jest algorytm z poprzedniego ćwiczenia

dane wejściowe:
    y - rok
"""

# wczytanie danych wejściowych
rok = int(input('Podaj rok: '))

dzien = 13
licznik = 0  # licznik piątków 13-tego
print('Piątki 13-tego wypadają:')
for miesiac in range(1, 13):
    if miesiac < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2
    numer_dnia_tygodnia = (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7
    if numer_dnia_tygodnia == 5:  # czy piątek?
        print('\tw miesiącu:', miesiac)
        licznik += 1

print('Liczba piątków 13-tego w', rok, 'r.:', licznik)
