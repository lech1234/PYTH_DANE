"""
skrypt przekształca listę miesięcy w nową listę w której miesiące są pogrupowane w półrocza
"""

# dowolna krotka
lista = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
         'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')
liczba_wierszy = 2
liczba_kolumn = len(lista) // liczba_wierszy

# tabela (macierz o wymiarach liczba_wierszy x dlugosc_wiersza)
tabela = [[element for indeks, element in enumerate(lista) if indeks // liczba_kolumn == numer_wiersza]
          for numer_wiersza in range(liczba_wierszy)]

# wypisanie listy półroczy
print('Półrocza:')
print(tabela, end='\n\n')

# wypisanie listy półroczy, każde półrocze w osobnej linii
print(*tabela, sep='\n')
