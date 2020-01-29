start_getallen = []
aantal_start_getallen = []

for x in range(0, 1000, 1):
    output = 2**x
    start_getallen.append(str(output)[0:1])
    print(output)
print()

for x in range(1, 10, 1):
    aantal_start_getallen.append(start_getallen.count(str(x)))
    print("Het getal " + str(x) + " komt " + str(start_getallen.count(str(x))) + " keer voor.")
print()

grafiek_max = 40
for x in aantal_start_getallen:
    output_string = ""
    for y in range(0, grafiek_max, 1):
        if y >= (x / 10):
            output_string += "-"
        else:
            output_string += "x"
    print(output_string)
print()