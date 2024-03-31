import random

# Gerar uma chave de criptografia aleatória
def gerador_chave():
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    chave = ''.join(random.sample(alfabeto, len(alfabeto)))
    return chave

# Criptografar uma mensagem usando a chave gerada
def criptografar(mensagem, chave):
    cripto = ""
    for char in mensagem:
        if char in chave:
            index = chave.index(char)
            cripto += chave[index-3]  
        else:
            cripto += char
    return cripto

# Descriptografar usando a chave gerada
def descriptografar(cripto, chave):
    mensagem = ""
    for char in cripto:
        if char in chave:
            index = chave.index(char)
            mensagem += chave[index+3]  
        else:
            mensagem += char
    return mensagem

# executar os comandos acima:
chave = gerador_chave()
print("Chave de criptografia gerada:", chave)

mensagem_original = "Eu te amo sua chata"
print("Mensagem original:", mensagem_original)

mensagem_criptografada = criptografar(mensagem_original, chave)
print("Mensagem criptografada:", mensagem_criptografada)

mensagem_descriptografada = descriptografar(mensagem_criptografada, chave)
print("Mensagem descriptografada:", mensagem_descriptografada)
