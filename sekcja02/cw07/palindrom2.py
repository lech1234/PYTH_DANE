"""
Moduł sprawdza, czy podany tekst jest palindromem.

ALternatywne rozwiązanie w stosunku do modułu palindrom1.
Porównywana jest pierwsza połowa listy z drugą połową w odwrotnej kolejności.
"""

if __name__ == '__main__':

    # Dane wejściowe (tekst do weryfikacji czy jest palindromem)
    tekst = 'Co mi dał duch? Cud, ład i moc.'
    print(tekst)

    # Budowa tekstu zawierającego tylko małe litery (duże litery są konwertwane na małe)
    tylko_litery = [znak.lower() for znak in tekst if znak.isalpha()]

    # Obliczenie indeksu środka tekstu
    n = len(tylko_litery) // 2

    # Porównanie lewej połowy tekstu z prawą połową napisaną wspak
    czy_palindrom = tylko_litery[:n] == tylko_litery[:-n - 1:-1]

    # Wypisanie wyniku weryfikacji
    print('Czy palindrom?', czy_palindrom)
