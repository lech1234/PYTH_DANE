"""
Moduł umożliwia 'sterowanie' robotem poruszającym się w 4 strony świata.

Polecenia dla robota wczytuje się z klawiatury.
Robot na bieżąco informuje o swoim położeniu.
"""
import math

if __name__ == '__main__':

    x = y = 0  # współrzędne początkowe robota

    while True:
        polecenie = input('Wydaj polecenie: ')

        # warunek wyjścia z nieskończonej pętli
        if not polecenie:  # równoważnie:    if polecenie == '':
            break

        kierunek, krok = polecenie.split()
        krok = int(krok)
        match kierunek:
            case 'E':
                x += krok
            case 'S':
                y -= krok
            case 'W':
                x -= krok
            case 'N':
                y += krok
            case _:
                continue

        print(f'Aktualne położenie robota: ({x}, {y})')

    print(f'\nRobot oddalił się od punktu startu na odległość {round(math.hypot(x, y), 2)}')
