novads_csv = open("aw_novads.csv", "r", encoding="utf-8")
pilsetas_csv = open("aw_pilseta.csv", "r", encoding="utf-8")


text_pilseta = pilsetas_csv.read()
text_novads = novads_csv.read()

pilseta_lines = text_pilseta.splitlines()
pilsetas = []
for line in pilseta_lines:
    pilseta = line.split(",")[2]
    vkur_cd = line.split(",")[3]
    pilsetas.append((pilseta, vkur_cd))


    

novads_lines =text_novads.splitlines()
novadi = []
for line in novads_lines:
    novads = line.split(",")[2]
    kods = line.split(",")[0]
    novadi.append((novads, kods))

meklet_pilsetu = input("Ievadiet pilsētu, kuru vēlaties meklēt: ")
meklet_pilsetu = meklet_pilsetu.lower()

atrasta = False
for pilseta, vkur_cd in pilsetas:
    if meklet_pilsetu in pilseta.lower():
        atrasta = True
        print(f"Pilsēta: {pilseta}, VKUR kods: {vkur_cd}")
        meklet_vkur_cd = vkur_cd
    
        if meklet_vkur_cd:
            for novads, kods in novadi:
                if meklet_vkur_cd == kods:
                    print(f"Pilsēta {pilseta} atrodas {novads}")
        
if not atrasta:
    print("Pilsēta netika atrasta.")





novads_csv.close()
pilsetas_csv.close()




