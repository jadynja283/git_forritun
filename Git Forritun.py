#Git verkefni Jadyn Margrét Jackson
print("1.")
print()

tala1 = int(input("Sláðu inn tölu 1 "))
tala2 = int(input("Sláðu inn tölu 2 "))

print("Hér eru tölurnar lagðar saman", tala1+tala2)
print("Hér eru tölurnar margfaldaðar saman", tala1*tala2)

print()
print("2.")
print()

fornafn = input("Fornafn? ")
eftirnafn = input("Eftirnafn? ")

print("Halló" ,fornafn, eftirnafn)

print()
print("3.")
print()

stor = 0 #Hástafir
litill = 0 #Lágstafir
eftir = 0 #Lágstafur á eftir hástaf
stada = -1 #Er notað til þess að talja hástaf á undan lágstaf
texti = input("Sláðu inn texta ")
lengd = int(len(texti)) #Notað til þess að keyra for-lykkjuna fyrir neðan integer

textlisti = list(texti)
print(textlisti)

for i in textlisti:
    if i.isupper() and i != ' ':
        stor += 1
    elif i.islower() and i != ' ':
        litill += 1


for x in range(lengd):
    if textlisti[x].islower() and textlisti[stada].isupper():
        stada += 1
        eftir += 1
    else:
        stada += 1

print("Í þessum texta eru" ,stor, "hástafir," ,litill, "lágstafir og" ,eftir, "lástafir koma strax á eftir hástaf." )

