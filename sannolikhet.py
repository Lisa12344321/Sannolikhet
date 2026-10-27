from random import randint

antal_tärningar = 6
gynnsamma_utfall = 0
möjliga_utfall = 20000

for i in range(möjliga_utfall):
    resultat = []
    for i in range(antal_tärningar):
        antal_prickar = randint(1, 6)
        resultat.append(antal_prickar)

    antal_fyror = resultat.count(4)
    if antal_fyror == 4:
        gynnsamma_utfall += 1

    procent = gynnsamma_utfall / möjliga_utfall * 100

    
    print(f"\nResultat: {resultat}")
    print(f"Antal fyror: {antal_fyror}")
    print(f"Gynnsamma utfall: {gynnsamma_utfall}")

print(f"\nSannolikheten är {gynnsamma_utfall} / {möjliga_utfall} = {round(gynnsamma_utfall/möjliga_utfall, 8)} = {round(procent, 5)} %")

