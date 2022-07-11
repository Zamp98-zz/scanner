import Tokens as t
from AnalisadorSintatico import AnalisadorSintatico 
 
tokens = t.getTokens('main.c')

fileOut = open("tokens.txt", 'w')

print(tokens)

for line in tokens:
    fileOut.write(line)
fileOut.write("$")
fileOut.close()

sintatico = AnalisadorSintatico()
sintatico.iniciar()