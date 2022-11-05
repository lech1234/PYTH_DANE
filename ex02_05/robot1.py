import math

x = y = 0  # współrzędne początkowe

while True:
    polecenie = input('Wydaj polecenie: ')
    if not polecenie:
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
    # W Pythonie < 3.10 zamiast instrukcji match trzeba zrobić:
    # if kierunek == 'E':
    #     x += krok
    # elif kierunek == 'S':
    #     y -= krok
    # elif kierunek == 'W':
    #     x -= krok
    # elif kierunek == 'N':
    #     y += krok
    # else:
    #     continue
    print(f'Bieżące położenie: ({x}, {y})')

print(f'\nOdległość od punktu startu: {round(math.hypot(x, y), 2)}')
