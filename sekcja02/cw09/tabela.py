"""
Moduł grupuje podany ciąg danych w tabelę o określonej liczbie wierszy.
To ten sam kod, co w module kwartaly4, jedynie z innymi nazwami zmiennych.
"""

if __name__ == '__main__':

    # Dowolna lista
    seria_danych = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
                    'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

    liczba_wierszy = 2
    liczba_danych = len(seria_danych)
    liczba_kolumn = liczba_danych // liczba_wierszy

    # Tabela (macierz o wymiarach liczba_wierszy x liczba_kolumn):
    tabela = [[element for indeks, element in enumerate(seria_danych)
               if indeks // liczba_kolumn == numer_wiersza]
              for numer_wiersza in range(liczba_wierszy)]

    # Wypisanie tabeli:
    print('Tabela:')
    print(*tabela, sep='\n')
