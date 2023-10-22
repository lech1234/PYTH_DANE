"""
Moduł oblicza szansę wylosowania zadanej liczby trafień w lotto.
Potrzebne dane będą wczytane z klawiatury.

Algorytm:
    jeśli losujemy k liczb spośród n różnych liczb, to:
    - 1-szą liczbę można wylosować na n sposobów, bo losujemy spośród n liczb
    - 2-gą na (n-1) sposobów, bo losujemy ze zbioru (n-1) liczb (jedną liczbę już wylosowaliśmy)
    - 3-cią na (n-2) sposobów, bo losujemy ze zbioru (n-2) liczb (dwie liczby już wylosowaliśmy)
    - itd...
    - ogólnie: k-tą liczbę losujemy na (n-k+1) sposobów

    czyli wszystkich możliwości jest: silnia(n) / silnia(n-k)

    Ponieważ k różnych liczb można ułożyć na silnia(k) sposobów,
    to ostatecznie poszukiwany wzór ma postać:

        silnia(n) / (silnia(n-k) * silnia(k))

"""

if __name__ == '__main__':

    import math

    # wczytanie danych wejściowych
    k = int(input('Ile liczb będziesz losował? '))
    n = int(input('Spośród ilu liczb? '))

    # wyliczenie liczby kombinacji:
    #     silnia(n) / (silnia(n-k) * silnia(k))
    liczba_kombinacji = math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

    # od Pythona 3.8 można prościej:
    # liczba_kombinacji = math.comb(n, k)

    # wypisanie wyniku
    print('Szansa na trafienie', k, 'liczb z', n, 'wynosi 1 do', liczba_kombinacji)
