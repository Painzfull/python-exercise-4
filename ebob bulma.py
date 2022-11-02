"""
ebob bulma programı

"""
def ebobb(sayı1,sayı2):
    i = 1
    ebob = 1
    while(i <= sayı1 and i <= sayı2):
        if(not (sayı1 % i ) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Birinci sayı değeri:"))
sayı2 = int(input("İkinci sayı değeri:"))

print("İki sayının ebobu:",ebobb(sayı1,sayı2))