"""
skrypt tworzy skrót na podstawie pierwszych dużych liter słów
np. dla:
United Nations Educational, Scientific and Cultural Organization --> UNESCO
"""

# dane wejściowe
pelna_nazwa = 'United Nations Educational, Scientific and Cultural Organization'

# budowa skrótu
krotka_nazwa = ''.join([slowo[0] for slowo in pelna_nazwa.split() if slowo[0].isupper()])

# wypisanie oryginalnej nazwy i jej skrótu
print(pelna_nazwa, '=', krotka_nazwa)
