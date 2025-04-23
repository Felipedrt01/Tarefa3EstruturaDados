print("=== É, ou não é palíndromo ===")

def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ")
    texto_formatado = ''.join(c.lower() for c in texto if c.isalnum())
    if texto_formatado == texto_formatado[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

verificar_palindromo()
