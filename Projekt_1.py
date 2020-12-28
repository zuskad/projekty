'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
uzivatele = {
	"bob": "123",
	"ann": "pass123",
	"mike": "password123",
    "liz": "pass123"
			}
oddelovac = (45 * "-")

print(oddelovac)
print("Vítejte v naší aplikaci. Přihlaste se prosím.")
print(oddelovac)
jmeno = input("Zadejte uživatelské jméno: ")
if jmeno not in uzivatele.keys():
    print("Chybné uživatelské jméno, ukončuji.")
    exit()
heslo = input("Zadejte heslo: ")
if heslo == uzivatele.get(jmeno):
    print("Zadané jméno a heslo jsou v pořádku.")
else:
    print("Chybné heslo, ukončuji.")
    exit()

print(oddelovac)
print("Budeme analyzovat 3 texty.")
mod = True
while mod == True:
    cislo = input("Zadejte číslo od 1 do 3 pro výběr textu: ")
    if not cislo.isnumeric():
        print("Opravte svou volbu, zadejte prosím pouze čísla od 1 do 3.")
        print(oddelovac)
    elif int(cislo) == 0:
        print("Opravte svou volbu, zadejte prosím pouze čísla od 1 do 3.")
        print(oddelovac)
    elif int(cislo) > 3:
        print("Opravte svou volbu, zadejte prosím pouze čísla od 1 do 3.")
        print(oddelovac)
    else:
        mod = False
        print(oddelovac)

text = TEXTS[int(cislo) - 1]
slova = text.split()
pomocna = text.split()

pocet_velka_pismena = 0
pocet_mala_pismena = 0
pocet_velke_pismeno = 0
pocet_cisel = 0

for i in slova:
    if i.istitle():
        pocet_velke_pismeno = pocet_velke_pismeno + 1
    if i.islower():
        pocet_mala_pismena = pocet_mala_pismena + 1
    if i.isupper():
        pocet_velka_pismena = pocet_velka_pismena + 1
    if i.isdigit():
        pocet_cisel = pocet_cisel + 1

print("Ve vybraném textu je celkem", len(slova), "slov.")
print("Ve vybraném textu je celkem", pocet_velke_pismeno, "slov začínajících velkým písmenem.")
print("Ve vybraném textu je celkem", pocet_mala_pismena, "slov psaných malými písmeny.")
print("Ve vybraném textu je celkem", pocet_velka_pismena, "slov psaných velkými písmeny.")
print("Počet čísel ve vybraném textu je:", str(pocet_cisel) + ".")

print(oddelovac)
print("Nyní následuje jednoduchý sloupcový graf zobrazující četnost délek slov v textu:")
print()

jedno = 0
dvou = 0
tri = 0
ctyr = 0
peti = 0
sesti = 0
sedmi = 0
osmi = 0
deviti = 0
desiti = 0
jedenacti = 0
dvanacti = 0
trinacti = 0

while pomocna:
    vyber = pomocna.pop().strip(" ,.")
    if len(vyber) == 1:
        jedno = jedno + 1
    elif len(vyber) == 2:
        dvou = dvou + 1
    elif len(vyber) == 3:
        tri = tri + 1
    elif len(vyber) == 4:
        ctyr = ctyr + 1
    elif len(vyber) == 5:
        peti = peti + 1
    elif len(vyber) == 6:
        sesti = sesti + 1
    elif len(vyber) == 7:
        sedmi = sedmi + 1
    elif len(vyber) == 8:
        osmi = osmi + 1
    elif len(vyber) == 9:
        deviti = deviti + 1
    elif len(vyber) == 10:
        desiti = desiti + 1
    elif len(vyber) == 11:
        jedenacti = jedenacti + 1
    elif len(vyber) == 12:
        dvanacti = dvanacti + 1
    elif len(vyber) == 13:
        trinacti = trinacti + 1


if jedno == 0:
    print(end="")
else:
    print("\t", "1", jedno * "*", jedno)

if dvou == 0:
    print(end="")
else:
    print("\t", "2", dvou * "*", dvou)

if tri == 0:
    print(end="")
else:
    print("\t", "3", tri * "*", tri)

if ctyr == 0:
    print(end="")
else:
    print("\t", "4", ctyr * "*", ctyr)

if peti == 0:
    print(end="")
else:
    print("\t", "5", peti * "*", peti)

if sesti == 0:
    print(end="")
else:
    print("\t", "6", sesti * "*", sesti)

if sedmi == 0:
    print(end="")
else:
    print("\t", "7", sedmi * "*", sedmi)

if osmi == 0:
    print(end="")
else:
    print("\t", "8", osmi * "*", osmi)

if deviti == 0:
    print(end="")
else:
    print("\t", "9", deviti * "*", deviti)

if desiti == 0:
    print(end="")
else:
    print("\t", "10", desiti * "*", desiti)

if jedenacti == 0:
    print(end=" ")
else:
    print("\t", "11", jedenacti * "*", jedenacti)

if dvanacti == 0:
    print(end="")
else:
    print("\t", "12", dvanacti * "*", dvanacti)

if trinacti == 0:
    print(end="")
else:
    print("\t","13", trinacti * "*", trinacti)

print()
print(oddelovac)

soucet = 0
while slova:
    vyber = slova.pop()
    if vyber.isdigit():
        soucet = soucet + int(vyber)
print("Pokud sečteme všechna čísla v tomto textu dostaneme číslo: ", soucet)

print(oddelovac)
