"""
Moduł oblicza, ile w danym roku wypada piątków 13-tego.

Do obliczeń wykorzystywany jest algorytm z poprzedniego ćwiczenia (2.2)
"""

if __name__ == '__main__':

    # wczytanie danych wejściowych
    rok = int(input('Podaj rok: '))

    licznik_piatkow_13tego = 0

    dzien = 13  # interesują nas tylko 13-te dni każdego miesiąca
    print('Piątki 13-tego wypadają w tym roku:')

    for miesiac in range(1, 13):  # trzeba sprawdzić, jakie dni tygodnia wypadają 13-tego dnia każdego miesiąca
        if miesiac < 3:
            z = rok - 1
            c = 0
        else:
            z = rok
            c = 2
        numer_dnia_tygodnia = (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7
        if numer_dnia_tygodnia == 5:  # czy to piątek?
            print('\tw miesiącu:', miesiac)
            licznik_piatkow_13tego += 1

    print(f'Liczba piątków 13-tego w {rok} r. wynosi {licznik_piatkow_13tego}')
