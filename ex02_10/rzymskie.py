"""
Skrypt zamienia liczbę arabską na rzymską.
"""

arabskie = 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
rzymskie = 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
zamiana = dict(zip(arabskie, rzymskie))

# dane wejściowe:
liczba = int(input('Podaj liczbę: '))

if 1 <= liczba < 4000:
    print(liczba, end='= ')
    rzymska = ''
    for arabska in arabskie:
        while liczba >= arabska:
            rzymska += zamiana[arabska]
            liczba -= arabska
        if liczba == 0:
            break
    print(rzymska)
else:
    print("Liczba musi mieścić się w przedziale od 1 do 3999")
