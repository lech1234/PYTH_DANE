"""
Moduł sprawdza, czy podany tekst jest palindromem.
"""

if __name__ == '__main__':

    # Dane wejściowe (tekst do weryfikacji czy jest palindromem)
    tekst = 'Co mi dał duch? Cud, ład i moc.'
    print(tekst)

    # Budowa tekstu zawierającego tylko małe litery (duże litery są konwertwane na małe)
    tylko_litery = [znak.lower() for znak in tekst if znak.isalpha()]

    # Weryfikacja czy lista liter i lista wspak są identyczne
    czy_palindrom = tylko_litery == tylko_litery[::-1]

    # Można też do utworzenia listy liter o odwrotnej kolejności użyć metody reverse()
    # Wtedy należy zastąpić linię 15 poniższymi:
    #
    # kopia_listy_liter = tylko_litery[:]
    # kopia_listy_liter.reverse()
    # czy_palindrom = tylko_litery == kopia_listy_liter

    # Wypisanie wyniku weryfikacji
    print('Czy palindrom?', 'TAK' if czy_palindrom else 'NIE')
