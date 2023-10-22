"""
Moduł wczytuje dane wejściowe z klawiatury, a następnie oblicza stan lokaty na koncie przy stałym oprocentowaniu
po upływie określonego czasu.
"""

if __name__ == '__main__':

    # pobranie danych wejściowych
    # funkcja input zwraca wartość w postaci tekstu, więc konieczna jest konwersja na typ liczbowy

    # dane początkowe:
    # lokata - kapitał początkowy
    # stopa  - oprocentowanie (podane w %) w skali roku
    # okres  - okres oszczędzania (podany w pełnych latach)
    #
    # algorytm:
    # stan lokaty po 0 latach: s0 = lokata
    # stan lokaty po 1 roku:   s1 = s0 * (1 + stopa / 100)
    # stan lokaty po 2 latach: s2 = s1 * (1 + stopa / 100) = s0 * (1 + stopa / 100) ** 2
    # stan lokaty po 3 latach: s3 = s2 * (1 + stopa / 100) = s0 * (1 + stopa / 100) ** 3
    # itd...
    # stan lokaty po n latach: sn = s0 * (1 + stopa / 100) ** n

    lokata = int(input('Podaj wartość początkową lokaty: '))
    stopa = float(input('Podaj roczną stopę oprocentowania [%]: '))
    okres = int(input('Podaj czas lokaty (w latach): '))

    # obliczenia: stan końcowy lokaty po zaokrągleniu do 2 miejsc w części ułamkowej
    kapital_koncowy = round(lokata * (1 + stopa / 100) ** okres, 2)

    # wypisanie wyniku
    print('\nStan lokaty po upływie', okres, 'lat oszczędzania wyniesie:', kapital_koncowy)
