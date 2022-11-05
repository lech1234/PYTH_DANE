"""
Skrypt z listy nazw miesięcy wypisuje te, które są początkami kwartałów.
"""

# krotka miesięcy
rok = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
       'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')

liczba_kwartalow = 4
dlugosc_kwartalu = len(rok) // liczba_kwartalow

# lista zawierająca nazwy miesięcy rozpoczynających kwartały
poczatki_kwartalow = [miesiac for nr_miesiaca, miesiac in enumerate(rok) if nr_miesiaca % dlugosc_kwartalu == 0]

# wypisanie elementów listy
print('Początki kwartałów:')
print(*poczatki_kwartalow, sep=', ', end='\n\n')

# to samo, ale prościej...
print('Początki kwartałów:')
print(*rok[::dlugosc_kwartalu], sep=', ')
