instrumentos = ["pinza", "tijera", "pinza"]
esperadas = 2
observadas = 0

for instrumento in instrumentos:
    if instrumento == "pinza":
        observadas = observadas + 1

print("Pinzas esperadas:", esperadas)
print("Pinzas observadas:", observadas)

if observadas < esperadas:
    print("Resultado: faltan pinzas")
elif observadas > esperadas:
    print("Resultado: sobran pinzas")
else:
    print("Resultado: coincide")
