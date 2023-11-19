"""
Moduł konwertuje wczytaną z klawiatury liczbę arabską na liczbę zapisaną cyframi rzymskimi.
"""

if __name__ == '__main__':

    # Krotki definujące wybrane liczby arabskie i ich odpowiedniki rzymskie:
    arabskie = 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    rzymskie = 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'

    # Słownik konwersji liczb arabskich na rzymskie utworzony na podstawie powyższych krotek:
    zamiana = dict(zip(arabskie, rzymskie))

    # Dane wejściowe:
    liczba = int(input('Podaj liczbę: '))

    # Weryfikacja, czy wczytana liczba mieści się w przedziale <1; 3999>
    if 1 <= liczba < 4000:
        print(liczba, end='= ')
        rzymska = ''

        # Iteracja po kolejnych liczbach arabskich w kolejności od największej do najmniejszej
        # Krotki sa uporządkowane, co gwarantuje zachowanie podanej kolejności
        for arabska in arabskie:
            # Pętla kontroluje, czy nie trzeba powtórzyć tej samej cyfry
            while liczba >= arabska:
                rzymska += zamiana[arabska]
                liczba -= arabska
            # Warunek przerywający pętlę, gdy zapis liczby jest już kompletny
            if liczba == 0:
                break
        print(rzymska)
    else:
        print('Liczba musi mieścić się w przedziale od 1 do 3999')
