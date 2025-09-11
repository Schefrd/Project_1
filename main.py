TEXTS = [
   """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.""",
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# prihlaseni
uzivatel = input("username: ").strip()
heslo = input("password: ").strip()

if uzivatel not in registrovani_uzivatele or registrovani_uzivatele[uzivatel] != heslo:
    print("unregistered user, terminating the program..")
    exit()

print("----------------------------------------")
print("Welcome to the app,", uzivatel)
print("We have", len(TEXTS), "texts to be analyzed.")
print("----------------------------------------")

# vyber textu
vyber = input("Enter a number btw. 1 and " + str(len(TEXTS)) + " to select: ").strip()
print("----------------------------------------")

if not vyber.isdigit():
    print("invalid input, terminating the program...")
    exit()

vyber = int(vyber)
if vyber < 1 or vyber > len(TEXTS):
    print("Number out of range, terminating the program..")
    exit()

text = TEXTS[vyber - 1]
slova = text.split()

# vypocet
pocet_slov = len(slova)
pocet_velkych = 0
pocet_velkymi = 0
pocet_malymi = 0
cisla = []

for s in slova:
    s_cista = s.strip(".,")
    if s_cista.istitle():
        pocet_velkych += 1
    if s_cista.isupper():
        pocet_velkymi += 1
    if s_cista.islower():
        pocet_malymi += 1
    if s_cista.isdigit():
        cisla.append(int(s_cista))

soucet_cisel = sum(cisla)
pocet_cisel = len(cisla)

# vysledky
print("There are", pocet_slov, "words in the selected text.")
print("There are", pocet_velkych, "titlecase words.")
print("There are", pocet_velkymi, "uppercase words.")
print("There are", pocet_malymi, "lowercase words.")
print("There are", pocet_cisel, "numeric strings.")
print("The sum of all the numbers:", soucet_cisel)
print("----------------------------------------")

# graf
delky = {}
for s in slova:
    delka = len(s.strip(".,"))
    if delka in delky:
        delky[delka] += 1
    else:
        delky[delka] = 1

print("LEN |     OCCURRENCES      | NR")
print("----------------------------------------")

for delka in sorted(delky.keys()):
    hvězdy = ""
    for i in range(delky[delka]):
        hvězdy += "*"
    print(f"{delka:3} | {hvězdy:<20} | {delky[delka]}")
