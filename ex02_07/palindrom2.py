"""
skrypt sprawdza, czy podany tekst jest palindromem
"""

# dane wejściowe (tekst do weryfikacji czy jest palindromem)
tekst = 'Co mi dał duch? Cud, ład i moc.'

# budowa tekstu zawierającego tylko małe litery (duże litery są konwertwane na małe)
tylko_litery = [znak.lower() for znak in tekst if znak.isalpha()]

# obliczenie indeksu środka tekstu
n = len(tylko_litery) // 2

# porównanie lewej połowy tekstu z prawą połową napisaną wspak
czy_palindrom = tylko_litery[:n] == tylko_litery[:-n - 1:-1]

# wypisanie wersji oryginalnej tekstu i wyniku weryfikacji
print(tekst)
print('Czy palindrom?', czy_palindrom)
