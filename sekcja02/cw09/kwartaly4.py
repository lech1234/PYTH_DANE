"""
Moduł przekształca listę miesięcy w nową listę w której miesiące są pogrupowane w kwartały.
"""

if __name__ == '__main__':

    # Lista nazw miesięcy:
    rok = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
           'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

    liczba_kwartalow = 4
    liczba_miesiecy = len(rok)
    dlugosc_kwartalu = liczba_miesiecy // liczba_kwartalow

    # Lista kwartałów:
    kwartaly = [[miesiac for nr_miesiaca, miesiac in enumerate(rok)
                 if nr_miesiaca // dlugosc_kwartalu == numer_kwartalu]
                for numer_kwartalu in range(liczba_kwartalow)]

    # Wypisanie listy kwartałów:
    print('Kwartały:')
    print(*kwartaly, sep='\n')
