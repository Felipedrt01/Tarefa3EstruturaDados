print("=== Contador de frequência numérica ===")

def count_freq():
    numeros = list(map(int, input("Digite números aleatórios separados por espaço: ").split()))
    alvo = int(input("Digite um o número, e saiba quantas vezes ele aparece: "))
    print("Ele aparece:", numeros.count(alvo), "vez(es).")

count_freq()
