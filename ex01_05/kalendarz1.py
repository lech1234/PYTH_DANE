"""
Wieczny kalendarz - skrypt oblicza jaki był dzień tygodnia danego dnia.

Autorem algorytmu jest Mike Keith.

Dane wejściowe:
    d - dzień miesiąca (1..31)
    m - miesiąc (1..12)
    y - rok

Algorytm:
zmienne pomocnicze
    z - jeśli m < 3 to: y - 1, w przeciwnym razie: y
    c - jeśli m < 3 to: 0, w przeciwnym razie: 2

Należy obliczyć wyrażenie:
    (czesc_calk(23*m/9) + d + 4 + y + czesc_calk(z/4) - czesc_calk(z/100) + czesc_calk(z/400) -c) mod 7
gdzie:
    czesc_calk(x) - oznacza część całkowitą x
Interpretacja wyniku:
    0 - niedziela, 1 - poniedziałek, ... , 6 - sobota
"""

# wczytanie danych wejściowych
dzien = int(input('Podaj dzień: '))
miesiac = int(input('Podaj miesiąc: '))
rok = int(input('Podaj rok: '))

# realizacja algorytmu
if miesiac < 3:
    z = rok - 1
    c = 0
else:
    z = rok
    c = 2
numer_dnia_tygodnia = (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7

# wypisanie wyniku algorytmu
print(dzien, miesiac, rok, sep=".", end=' to ')

# interpretacja wyniku w postaci nazwy dnia tygodnia
match numer_dnia_tygodnia:
    case 0:
        print('niedziela')
    case 1:
        print('poniedziałek')
    case 2:
        print('wtorek')
    case 3:
        print('środa')
    case 4:
        print('czwartek')
    case 5:
        print('piątek')
    case 6:
        print('sobota')

# powyższa konstrukcja działa od wersji 3.10

# w starszych wersjach można użyć konstrukcji if-elif-else
# if numer_dnia_tygodnia == 0:
#     print('niedziela')
# elif numer_dnia_tygodnia == 1:
#     print('poniedziałek')
# elif numer_dnia_tygodnia == 2:
#     print('wtorek')
# elif numer_dnia_tygodnia == 3:
#     print('środa')
# elif numer_dnia_tygodnia == 4:
#     print('czwartek')
# elif numer_dnia_tygodnia == 5:
#     print('piątek')
# elif numer_dnia_tygodnia == 6:
#     print('sobota')
