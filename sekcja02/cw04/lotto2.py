"""
Moduł oblicza szansę wylosowania zadanej liczby trafień w lotto.
Potrzebne dane będą wczytane z klawiatury.

Jest to zoptymalizowana wersja rozwiązania z modułu lotto1
"""

if __name__ == '__main__':

    # Wczytanie danych wejściowych:
    k = int(input('Ile liczb będziesz losował? '))
    n = int(input('Spośród ilu liczb? '))

    # Obliczenia:
    # - analizując poprzednie rozwiązanie można zauważyć, że obie pętle są wykonywane tę samą ilość razy.
    # - wtedy do obliczenia obu wyrażeń można użyć jednej pętli
    wyrazenie1 = 1
    wyrazenie2 = 1
    delta = n - k
    for liczba in range(1, k + 1):
        wyrazenie1 *= liczba
        wyrazenie2 *= liczba + delta

    # Wyliczenie liczby kombinacji:
    liczba_kombinacji = wyrazenie2 // wyrazenie1

    # Wypisanie wyniku:
    print(f'Szansa na trafienie {k} liczb spośród {n} wynosi 1 : {liczba_kombinacji:,}')
