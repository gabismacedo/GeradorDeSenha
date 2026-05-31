"""
GERADOR DE SENHA 

- números
- caracteres especiais
- letrar maiusculas e minusculas
- quatidade minima de 12 
- clicar em algum lugar para criar essas senhas
"""

import secrets
import string

def gerar_senha(qtd=12):

    """ 
    ascii_letters: sequencia de letras maiusculas e minusculas
    string.digits: sequencia de numeros de 0 a 9
    string.punctuation: sequencia de caracteres especiais
    """

    letras = string.ascii_letters + string.digits + string.punctuation
    caracteres = r"%&'()+,-./:;<=>[\]^_`{|}~"

    # escolha_qtd = int(input('escolha uma quatidade de caracteres: '))

    for retirar_caracter in caracteres:
        letras = letras.replace(retirar_caracter, '')
    
    token = ''.join(secrets.choice(letras) for _ in range (qtd))
    return token 
