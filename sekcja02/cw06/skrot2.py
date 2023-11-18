"""
Moduł tworzy skrót na podstawie pierwszych dużych liter słów.

Na przykład dla:
    United Nations Educational, Scientific and Cultural Organization --> UNESCO

Rozwiązanie alternatywne dla modułu skrot1, prezentujące wykorzystanie operatora :=
"""

if __name__ == '__main__':

    # Dane wejściowe
    pelna_nazwa = 'United Nations Educational, Scientific and Cultural Organization'

    # Budowa skrótu (użyto operatora := który dostępny jest od Python'a 3.8+)
    krotka_nazwa = ''.join([inicjal for slowo in pelna_nazwa.split() if (inicjal := slowo[0]).isupper()])

    # Wypisanie oryginalnej nazwy i jej skrótu
    print(pelna_nazwa, '=', krotka_nazwa)
