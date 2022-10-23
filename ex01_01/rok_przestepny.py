"""
Program sprawdza, czy podany rok jest przestępny
"""

# wprowadzenie danych wejściowych
rok = int(input('Podaj rok: '))

# obliczenia
# wyrażenie zwraca wartość logiczną
czy_przestepny = (rok % 400 == 0) or (rok % 100 != 0) and (rok % 4 == 0)

# wypisanie wyniku
print('Czy rok', rok, 'jest przestępny?', czy_przestepny)
