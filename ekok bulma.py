"""
ekok bulma programı

"""


def ekokk(sayı1,sayı2):

    i = 2
    ekok = 1
    while True:

        if(sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i

        elif(sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i
        elif(sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if(sayı1 == 1 and sayı2 == 1):
            break

    return ekok

sayı1 = int(input("Birinci sayı:"))
sayı2 = int(input("İkinci sayı:"))

print("Seçilen sayıların ekoku:",ekokk(sayı1,sayı2))

