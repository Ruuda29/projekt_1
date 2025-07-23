"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Březina
email: brezinajan@proton.me
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
    "bob": 123, 
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
oddelovac = 45 * "-"

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")
print(oddelovac)

if username in uzivatele and str(uzivatele[username]) == password:
    print(
    f"Welcome to the app, {username}\n"
    f"We have {len(TEXTS)} texts to be analyzed.\n"
    f"{oddelovac}"
    )
elif username not in uzivatele:
    print(
    f"Uzivatel {username} není registrován!\n"
    f"Ukončuji program!"
    )
    quit()
else:
    print(
    f"Špatně zadané heslo!\n"
    f"Ukončuji program!"
    )
    quit()

# Výběr textu
cislo_textu = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(oddelovac)

if (
    not cislo_textu.isnumeric()
    or int(cislo_textu) < 1
    or int(cislo_textu) > len(TEXTS)
):
    print(
    f"Špatně zvolený text!\n"
    f"Ukončuji program!"
    )
    quit()

# Práce s textem
zvoleny_text = TEXTS[int(cislo_textu) - 1]
rozdeleny_text = zvoleny_text.replace(".", "").replace(",", "").split()

## Počet slov
pocet_slov = len(rozdeleny_text)
print(f"There are {pocet_slov} words in the selected text.")

## Slova začínající na velké písmeno
velke_pismeno_na_zacatku = [slovo for slovo in rozdeleny_text if slovo.istitle()]
print(f"There are {len(velke_pismeno_na_zacatku)} titlecase words.")

## Slova obsahující pouze velká písmena
pouze_velka_pismena = [slovo for slovo in rozdeleny_text if slovo.isupper()]
print(f"There are {len(pouze_velka_pismena)} uppercase words.")

## Slova obsahující pouze malá písmena
pouze_mala_pismena = [slovo for slovo in rozdeleny_text if slovo.islower()]
print(f"There are {len(pouze_mala_pismena)} lowercase words.")

## Počet čísel
cisla_v_textu = [int(slovo) for slovo in rozdeleny_text if slovo.isnumeric()]
print(f"There are {len(cisla_v_textu)} numeric strings.")

## Suma čísel
print(f"The sum of all the numbers {sum(cisla_v_textu)}.")

print(oddelovac)

## Výskyt slov
print(
    f"LEN|{'OCCURRENCES'.center(25)}|NR.\n"
    f"{oddelovac}"
)

vyskyt_slov = {}

for slovo in rozdeleny_text:
    if len(slovo) not in vyskyt_slov:
        vyskyt_slov[len(slovo)] = 1
    else:
        vyskyt_slov[len(slovo)] += 1

usporadany_vyskyt_slov = dict(sorted(vyskyt_slov.items()))

for key, value in usporadany_vyskyt_slov.items():
    print(
        f"{str(key).rjust(3)}|"
        f"{str(value * "*").ljust(25)}"
        f"|{value}"
    )