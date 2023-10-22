"""
Moduł wczytuje z klawiatury rok i sprawdza, czy jest on przestępny.
W rozwiązaniu użyto wyrażenie logiczne (zamiast instrukcji warunkowych).
"""

if __name__ == '__main__':

    # Wprowadzenie danych wejściowych
    rok = int(input('Podaj rok: '))

    # Obliczenia
    # Wyrażenie zwraca wartość logiczną
    czy_rok_przestepny = rok % 400 == 0 or rok % 100 != 0 and rok % 4 == 0

    # Wypisanie wyniku
    print('Czy rok', rok, 'jest przestępny?', czy_rok_przestepny)
