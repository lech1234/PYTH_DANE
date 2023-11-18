"""
Moduł tworzy skrót na podstawie pierwszych dużych liter słów.

Przykładowo dla:
    United Nations Educational, Scientific and Cultural Organization --> UNESCO
"""

if __name__ == '__main__':

    # dane wejściowe
    pelna_nazwa = 'United Nations Educational, Scientific and Cultural Organization'

    # budowa skrótu
    krotka_nazwa = ''   # zmienna zawierająca docelowo skrót

    for slowo in pelna_nazwa.split():
        inicjal = slowo[0]
        if inicjal.isupper():
            krotka_nazwa += inicjal

    # wypisanie oryginalnej nazwy i jej skrótu
    print(pelna_nazwa, '=', krotka_nazwa)
