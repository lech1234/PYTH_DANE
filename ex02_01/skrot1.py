"""
Skrypt tworzy skrót na podstawie pierwszych dużych liter słów.

Przykładowo dla:
    United Nations Educational, Scientific and Cultural Organization --> UNESCO
"""

# dane wejściowe
pelna_nazwa = 'United Nations Educational, Scientific and Cultural Organization'

# budowa skrótu
krotka_nazwa = ''   # zmienna zawierająca skrót
for slowo in pelna_nazwa.split():
    pierwszy_znak = slowo[0]
    if pierwszy_znak.isupper():
        krotka_nazwa += pierwszy_znak

# wypisanie oryginalnej nazwy i jej skrótu
print(pelna_nazwa, '=', krotka_nazwa)
