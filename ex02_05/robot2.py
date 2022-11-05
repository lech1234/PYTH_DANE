pozycja = 0
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
    print(f'Bieżące położenie: ({x}, {y})')
print(f'\nOdległość od punktu startu: {round(abs(pozycja), 2)}')
