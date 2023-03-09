L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

paire=0

for nombre in L:
    if nombre%2==0:
        paire = paire + nombre

print(paire)