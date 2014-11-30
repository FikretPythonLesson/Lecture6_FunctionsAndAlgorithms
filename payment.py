# -*- coding: cp1254 -*-
toplamS = input("çalışma saatini girin")
saatUcreti = input("saat ücretini girin")

if toplamS <= 40:
    normalS = toplamS
    mesaiS = 0
else:
    normalS = 40
    mesaiS = toplamS - 40

toplamUcret = (normalS * saatUcreti) + ((mesaiS * saatUcreti) * 1.5)
print toplamUcret

