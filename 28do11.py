""""

frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
print("")
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

# ---------------------------------------------------------

frutas.append("pera")
print(frutas)

# ---------------------------------------------------------

frutas.insert(1, "uva")
print(frutas)

# ---------------------------------------------------------

frutas.remove("banana")
print(frutas)

# ---------------------------------------------------------

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

# ---------------------------------------------------------

frutas.sort()
print(frutas)

# ---------------------------------------------------------

frutas.reverse()
print(frutas)



for fruta in frutas:
    print(fruta)
    
"""

contador = 0

'''

while contador <= 5:
    print(contador)
    contador += 1

'''

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break
