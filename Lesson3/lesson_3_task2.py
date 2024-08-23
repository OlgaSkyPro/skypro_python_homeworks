from smartphone import Smartphone

catalog = []
phon1 = Smartphone("Sumsung", "M-555", "+79001234567")
phon2 = Smartphone("Nokia", "N-1313", "+79009995566")
phon3 = Smartphone("Sumsung", "X-SUPER", "+79007778899")
phon4 = Smartphone("LG", "L-01", "+79005556677")
phon5 = Smartphone("Xmi", "S-555", "+79005559988")


catalog = [phon1, phon2, phon3, phon4, phon5]

l=len(catalog)
i=0
for i in range (0,l,1):
    #i=i+1
    phon=catalog[i]
    #print (phon)
    phon.PrintName()
