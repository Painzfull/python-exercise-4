"""
sayının tam bölenlerini bulma
"""
def tambölenleribulma(sayı):
    tam_bölenler = []

    for i in range (1,sayı+1):
        if(sayı % i == 0):
            tam_bölenler.append(i)
    return tam_bölenler
while True:

    sayı = input("Sayı:")

    if(sayı == "q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        print("Tam bölenler:",tambölenleribulma(sayı))

