betaling = input()
totaal = int(betaling)
kassa = [500, 200, 100, 50, 20, 10, 5]
terug = []
i = 0
while i < len(kassa):
    if totaal >= kassa[i]:
        terug.append(kassa[i])
        totaal -= kassa[i]
    if totaal < kassa[i]:
        i = i + 1
    if totaal <= 4:
        print(str(terug).strip('[]'))
        break;