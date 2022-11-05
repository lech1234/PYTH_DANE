"""
Skrypt oblicza szansę zadanej liczby trafień w lotto.

Wyrażenie, które należy obliczyć to (p. ćwiczenie 3.3):
        silnia(n) / (silnia(n-k) * silnia(k))
gdzie:
    n - pula liczb z której losujemy
    k - ilość losowanych liczb

W rozwiązaniu do wyliczenia silni użyte zostały pętle
"""


# wczytanie danych wejściowych
k = int(input('Ile liczb będziesz losował? '))
n = int(input('Spośród ilu liczb? '))

# wyliczenie wyrażenia 1:
#    silnia(k) = 1 * 2 * ... * k
wyrazenie1 = 1
for liczba in range(1, k + 1):
    wyrazenie1 *= liczba

# wyliczenie wyrażenia 2:
#    silnia(n) / silnia(n - k) = (n - k + 1) * (n - k + 2) * ... * (n -1) * n
wyrazenie2 = 1
for liczba in range(n - k + 1, n + 1):
    wyrazenie2 *= liczba

# wyliczenie liczby kombinacji:
liczba_kombinacji = wyrazenie2 // wyrazenie1

# wypisanie wyniku
print(f'Szansa na trafienie {k} liczb z {n} wynosi 1 : {liczba_kombinacji:,}')
