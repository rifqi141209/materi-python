#program membuat persegi dengan inpu dari user
#contoh persegi
#    *****
#    *****
#    *****
#    *****
#    *****
#misal 
sisi = int(input("masukan papanjang sisi : "))
#membuat persegi dengan simbol bintang 
for udin in range(sisi):
    bintang =""
    for asep in range(sisi):
        bintang +="*"
    print(bintang)