novads_csv = open("aw_novads.csv", "r", encoding="utf-8")
pilsetas_csv = open("aw_pilseta.csv", "r", encoding="utf-8")


text_pilseta = pilsetas_csv.read()
text_novads = novads_csv.read()

novadi = {}
for line in text_novads.splitlines():
    novads = line.split(",")[2]
    kods = line.split(",")[0]
    novadi[kods] = novads

pilsetas = {}

for line in text_pilseta.splitlines():
    pilseta = line.split(",")[2]
    vkur_cd = line.split(",")[3]
    pilsetas[vkur_cd] = pilseta

meklet_pilsetu = input("Ievadiet pilsētu, kuru vēlaties meklēt: ").lower()
atrasta = False
for vkur_cd, pilseta in pilsetas.items():
    if meklet_pilsetu in pilseta.lower():
        print(f"Pilsēta: {pilseta}, VKUR kods: {vkur_cd}")
        atrasta = True
        if vkur_cd in novadi:
            print(f"Pilsēta {pilseta} atrodas {novadi[vkur_cd]}")

if not atrasta:
    print("Pilsēta netika atrasta.")

novads_csv.close()
pilsetas_csv.close()