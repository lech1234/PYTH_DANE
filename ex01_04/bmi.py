"""
Moduł wylicza indeks BMI (Body Mass Index), stawia diagnozę oraz wylicza graniczne wartości prawidłowej wagi.

Jeśli indeks...
        < 16.00 – wygłodzenie
    16.00–16.99 – wychudzenie
    17.00–18.49 – niedowaga
    18.50–24.99 – wartość prawidłowa
    25.00–29.99 – nadwaga
    30.00–34.99 – I stopień otyłości
    35.00–39.99 – II stopień otyłości (otyłość kliniczna)
        ≥ 40.00 – III stopień otyłości (otyłość skrajna)
"""

# pobranie danych wejściowych
wzrost = float(input('Podaj swój wzrost [m]: '))
waga = float(input('Podaj swoją wagę [kg]: '))

# wyliczenie indeksu i zaokrąglenie do 2 miejsc po przecinku
bmi = round(waga / wzrost / wzrost, 2)

# wypisanie wartości indeksu
print('Twój indeks BMI wynosi: ', bmi)

# interpretacja tekstowa liczbowej wartości indeksu
print('Diagnoza: ', end='')
if bmi < 16:
    print('wygłodzenie')
elif bmi < 17:
    print('wychudzenie')
elif bmi < 18.5:
    print('niedowaga')
elif bmi < 25:
    print('wartość prawidłowa')
elif bmi < 30:
    print('nadwaga')
elif bmi < 35:
    print('I stopień otyłości')
elif bmi < 40:
    print('II stopień otyłości (otyłość kliniczna)')
else:
    print('III stopień otyłości (otyłość skrajna)')

# obliczenie przedziału prawidłowej wagi przy posiadanym wzroście
ok_min = round(18.5 * wzrost ** 2, 1)
ok_max = round(24.99 * wzrost ** 2, 1)

# wypisanie obliczonego przedziału
print('Przy twoim wzroście:', ok_min, '<= prawidłowa waga <=', ok_max)
