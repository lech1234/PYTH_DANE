"""
Moduł tworzy skrót na podstawie pierwszych dużych liter słów.

Na przykład dla:
    United Nations Educational, Scientific and Cultural Organization --> UNESCO
"""

if __name__ == '__main__':

    # Dane wejściowe
    pelna_nazwa = 'United Nations Educational, Scientific and Cultural Organization'

    # Budowa skrótu
    krotka_nazwa = ''.join([slowo[0] for slowo in pelna_nazwa.split() if slowo[0].isupper()])

    # Wypisanie oryginalnej nazwy i jej skrótu
    print(pelna_nazwa, '=', krotka_nazwa)
