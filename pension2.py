# -*- coding: cp1254 -*-

cinsiyet = raw_input("Cinsiyet E/K:")
yas = int(raw_input("Yas:"))

if cinsiyet == 'E'
    if yas >= 65 and yas < 70:
        toplamOdeme = 5000
    elif yas >= 70:
        toplamOdeme = 5000 + 2000
    elif yas < 65:
        toplamOdeme = 0
elif cinsiyet == 'K'
    if yas >= 65:
        toplamOdeme = 4500 + 2500
    elif yas >= 60 and yas < 65:
        toplamOdeme = 4500
    elif yas < 60:
        toplamOdeme = 0

print toplamOdeme
