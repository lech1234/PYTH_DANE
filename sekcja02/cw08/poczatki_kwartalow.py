"""
Moduł, z listy nazw miesięcy wypisuje te, które są początkami kwartałów.
"""

if __name__ == '__main__':
    # Krotka miesięcy
    rok = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
           'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')

    liczba_kwartalow = 4
    dlugosc_kwartalu = len(rok) // liczba_kwartalow

    # Lista zawierająca nazwy miesięcy rozpoczynających kwartały
    poczatki_kwartalow = [miesiac for nr_miesiaca, miesiac in enumerate(rok) if nr_miesiaca % dlugosc_kwartalu == 0]

    # To samo, ale prościej...
    poczatki_kwartalow = rok[::dlugosc_kwartalu]

    # Wypisanie elementów listy
    print('Początki kwartałów:')
    print(*poczatki_kwartalow, sep=', ')
