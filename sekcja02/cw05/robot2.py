"""
Moduł umożliwia 'sterowanie' robotem poruszającym się w 4 strony świata.

Polecenia dla robota wczytuje się z klawiatury.
Robot na bieżąco informuje o swoim położeniu.

Alternatywne rozwiązanie w stosunku do modułu robot1, wykorzystujące liczby zespolone.
"""

if __name__ == '__main__':

    # położenie robota opisuje jedna liczba zespolona
    # współrzędna x to część rzeczywista, zaś współrzędna y to część urojona
    pozycja = 0 + 0j

    # jednostka określająca kierunek
    mnoznik = {'E': 1, 'S': -1j, 'W': -1, 'N': 1j}

    while True:
        polecenie = input('Wydaj polecenie: ')
        if not polecenie:
            break

        kierunek, krok = polecenie.split()
        krok = int(krok)

        if kierunek in mnoznik.keys():
            pozycja += mnoznik[kierunek] * krok

        x, y = pozycja.real, pozycja.imag
        print(f'Aktualne położenie robota: ({x}, {y})')

    print(f'\nRobot oddalił się od punktu startu na odległość {round(abs(pozycja), 2)}')
