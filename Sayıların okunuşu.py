"""
sayı okunuşu bulma programı
"""
birlik = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onluk = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def sayı_okunuşu(sayı):
    bir = sayı % 10
    iki = sayı // 10
    return onluk[iki] + " " + birlik[bir]

sayı = int(input("sayı:"))
if(sayı == 31):
    print(sayı_okunuşu(31),"sj")
else:
    print(sayı_okunuşu(sayı))



