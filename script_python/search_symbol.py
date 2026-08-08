import lief


# ---------------------------------------------------------
# PROCURAR stringFromJNI
# ---------------------------------------------------------

SO_FILE = r"C:\Users\lucio\Documents\engenharia_reversa\libpeelfresearch.so"


binary = lief.parse(SO_FILE)

print("\n" + "=" * 70)
print("PROCURANDO stringFromJNI")
print("=" * 70)

encontrado = False

for symbol in binary.symbols:
    if "stringFromJNI" in symbol.name:
        print("Encontrado:")
        print("Nome:", symbol.name)
        print("VA:", hex(symbol.value))
        print("Endereço:", hex(symbol.value))
        print("Tamanho:", symbol.size)

        encontrado = True

if not encontrado:
    print("stringFromJNI não apareceu nos símbolos.")