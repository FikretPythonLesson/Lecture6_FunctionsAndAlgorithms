# -*- coding: cp1254 -*-
bolge = raw_input("Bölgeyi girin")
hiz = int(raw_input("Hızı girin"))

if bolge == 'SI' and hiz < 60:
    odenecek = 0
elif bolge == 'SI' and hiz == 60:
    odenecek = 5000
elif bolge == 'SI' and hiz > 60:
    odenecek = 5000 + (500 * (hiz - 60))
elif bolge == 'SD' and hiz < 90:
    odenecek = 0
elif bolge == 'SD' and hiz == 90:
    odenecek = 1000
elif bolge == 'SD' and hiz > 90:
    odenecek = 1000 + (100 * (hiz - 90))
elif bolge == 'OY' and hiz < 130:
    odenecek = 0
elif bolge == 'OY' and hiz == 130:
    odenecek = 500
elif bolge == 'OY' and hiz > 130:
    odenecek = 500 + (50 * (hiz - 130))

print odenecek
    
