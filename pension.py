# -*- coding: cp1254 -*-
##Ekosul1 = E ve yaşı >= 65
##Ekosul2 = E ve yaşı >= 70
##EKosul3 = E ve yaşı < 65
##
##Kkosul1 = K ve yaşı >= 60
##Kkosul2 = K ve yaşı >= 65
##Kkosul3 = K ve yaşı < 60


for _ in range(10):
    cinsiyet = raw_input("Cinsiyet E/K:")
    yas = int(raw_input("Yas:"))

    if cinsiyet == 'E' and yas >= 65 and yas < 70:
        toplamOdeme = 5000
    elif cinsiyet == 'E' and yas >= 70:
        toplamOdeme = 5000 + 2000
    elif cinsiyet == 'E' and yas < 65:
        toplamOdeme = 0
    elif cinsiyet == 'K' and yas >= 65:
        toplamOdeme = 4500 + 2500
    elif cinsiyet == 'K' and yas >= 60 and yas < 65:
        toplamOdeme = 4500
    elif cinsiyet == 'K' and yas < 60:
        toplamOdeme = 0
