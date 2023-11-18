"""
Moduł oblicza szansę wylosowania zadanej liczby trafień w lotto.
Potrzebne dane będą wczytane z klawiatury.

Wyrażenie, które należy obliczyć to (p. ćwiczenie 1.3):
        silnia(n) / (silnia(n-k) * silnia(k))
gdzie:
    n - pula liczb z której losujemy
    k - ilość losowanych liczb

W rozwiązaniu do wyliczenia silni użyte zostały pętle.
"""

if __name__ == '__main__':

    # Wczytanie danych wejściowych:
    k = int(input('Ile liczb będziesz losował? '))
    n = int(input('Spośród ilu liczb? '))

    # Wyliczenie wyrażenia 1:
    #    silnia(k) = 1 * 2 * ... * k
    wyrazenie1 = 1
    for liczba in range(1, k + 1):
        wyrazenie1 *= liczba

    # Wyliczenie wyrażenia 2:
    #    silnia(n) / silnia(n - k) = (n - k + 1) * (n - k + 2) * ... * (n -1) * n
    wyrazenie2 = 1
    for liczba in range(n - k + 1, n + 1):
        wyrazenie2 *= liczba

    # Wyliczenie liczby kombinacji:
    liczba_kombinacji = wyrazenie2 // wyrazenie1

    # Wypisanie wyniku:
    print(f'Szansa na trafienie {k} liczb spośród {n} wynosi 1 : {liczba_kombinacji:,}')
