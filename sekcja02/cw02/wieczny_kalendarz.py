"""
Moduł oblicza na podstawie wczytanej z klawiatury daty, jaki był dzień tygodnia danego dnia.

Autorem algorytmu jest Mike Keith.

Jest to uproszczenie kodu rozwiązania ćwiczenia 1.5, dzięki zastosowaniu krotek.
"""

if __name__ == '__main__':

    # wczytanie danych wejściowych
    dzien = int(input('Podaj dzień: '))
    miesiac = int(input('Podaj miesiąc: '))
    rok = int(input('Podaj rok: '))

    # realizacja algorytmu
    if miesiac < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2

    numer_dnia_tygodnia = (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7

    # wypisanie wyniku algorytmu
    print(dzien, miesiac, rok, sep=".", end=' ')

    # interpretacja wyniku w postaci nazwy dnia tygodnia
    tydzien = 'niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'
    print('to', tydzien[numer_dnia_tygodnia])
