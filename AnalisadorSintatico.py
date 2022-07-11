import os.path

class AnalisadorSintatico():
    def __init__(self):

        self.arquivo_entrada = "tokens.txt"
        self.arquivo_saida = "resposta.txt"

        self.tem_erro_sintatico = False

        self.arquivo_saida = open(self.arquivo_saida, 'w')
        if not os.path.exists(self.arquivo_entrada):
            print("Arquivo de entrada inexistente")
            self.arquivo_saida.write("Arquivo de entrada inexistente")
            return

        self.arquivo = open(self.arquivo_entrada, 'r')
        self.tokens = self.arquivo.readlines()
        self.arquivo.close()
        self.i = 0
        self.j = 0
        self.linha_atual = ""

    def next_token(self):
        self.i += 1
        self.linha_atual = self.tokens[self.i][self.tokens[self.i].find('->') + 2: -1]
        
    def conteudo_token(self):
        return self.tokens[self.i][: self.tokens[self.i].find('->')]

    def iniciar(self):

        if ("Erro Lexico" in self.tokens[self.i]):
            self.i += 1

        self.main_declaracao()
        
        if (self.tem_erro_sintatico):
            print("Verifique os erros sintaticos e tente compilar novamente")
            self.arquivo_saida.write("Verifique os erros sintaticos e tente compilar novamente\n")
        else:
            if ("$" in self.tokens[self.i]):
                print("Cadeia de tokens na analise sintatica reconhecida com sucesso")
                self.arquivo_saida.write("Cadeia de tokens reconhecida com sucesso\n")
            else:
                print("Fim de Programa Nao Encontrado!")
                self.arquivo_saida.write("Fim de Programa Nao Encontrado!")

        self.arquivo_saida.close()

    def main_declaracao(self):
        if ("Erro Lexico" in self.tokens[self.i]):
            self.i += 1

        if('type_' in self.tokens[self.i]):
            self.next_token()

            if ('reserved_main' in self.tokens[self.i]):
                self.next_token()
                if ('parenthesis_(' in self.tokens[self.i]):
                    self.next_token()
                    if ('parenthesis_)' in self.tokens[self.i]):
                        self.next_token()
                        if ('brackets_{' in self.tokens[self.i]):
                            self.next_token()
                            while(self.variaveis_declaracao()):
                                pass
                            if ('brackets_}' in self.tokens[self.i]):
                                self.next_token()
                            else:
                                print("Erro sintatico - Esperado '}'  - linha: " + self.linha_atual + "\n")
                                self.arquivo_saida.write("Erro sintatico  - Esperado '}' - linha: " + self.linha_atual + "\n")
                                print('Token problemático: ' + self.tokens[self.i])
                                self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
                                self.tem_erro_sintatico = True
                        else:
                            print("Erro sintatico - Esperado '{' - linha: " + self.linha_atual + "\n")
                            self.arquivo_saida.write("Erro sintatico - Esperado '{'  - linha: " + self.linha_atual + "\n")
                            print('Token problemático: ' + self.tokens[self.i])
                            self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
                            self.tem_erro_sintatico = True
                else:
                    print("Erro sintatico - Esperado um 'identificador' - linha: " + self.linha_atual + "\n")
                    self.arquivo_saida.write(
                        "Erro sintatico  - Esperado um 'identificador' - linha: " + self.linha_atual + "\n")
                    print('Token problemático: ' + self.tokens[self.i])
                    self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
                    self.tem_erro_sintatico = True
                    return
        else:
            print("Erro sintatico - Esperado um 'identificador' - linha: " + self.linha_atual + "\n")
            self.arquivo_saida.write(
                "Erro sintatico  - Esperado um 'identificador' - linha: " + self.linha_atual + "\n")
            print('Token problemático: ' + self.tokens[self.i])
            self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
            self.tem_erro_sintatico = True
            return

    def variaveis_declaracao(self):
        if ("Erro Lexico" in self.tokens[self.i]):
            self.i += 1
        if ('type_' in self.tokens[self.i]):
            self.next_token()
            if ('attrib_=' in self.tokens[self.i]):
                self.next_token()
                if ("expression_;" in self.tokens[self.i]):
                    self.next_token()
                    return True
                elif ('brackets_}' in self.tokens[self.i]):
                    return False
                else:
                    self.arquivo_saida.write(
                        "Erro sintatico - Esperado símbolo ';' ao final do bloco de variáveis - linha: " + self.linha_atual + "\n")
                    print(
                        "Erro sintatico - Esperado símbolo ';' ao final do bloco de variáveis - linha: " + self.linha_atual + "\n")
                    self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
                    print('Token problemático: ' + self.tokens[self.i])
                    self.tem_erro_sintatico = True
            else:
                print(
                    "Erro sintatico - Esperado símbolo '=' após a declaração de variáveis - linha: " + self.linha_atual + "\n")
                self.arquivo_saida.write(
                    "Erro sintatico - Esperado símbolo '=' após a declaração de variáveis - linha: " + self.linha_atual + "\n")
                print('Token problemático: ' + self.tokens[self.i])
                self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
                self.tem_erro_sintatico = True
        if ('reserved_return' in self.tokens[self.i]):
            self.next_token()
            
            if ("expression_;" in self.tokens[self.i]):
                self.next_token()
                return False
            else:
                self.arquivo_saida.write(
                    "Erro sintatico - Esperado símbolo ';' ao final do bloco de variáveis - linha: " + self.linha_atual + "\n")
                print(
                    "Erro sintatico - Esperado símbolo ';' ao final do bloco de variáveis - linha: " + self.linha_atual + "\n")
                self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
                print('Token problemático: ' + self.tokens[self.i])
                self.tem_erro_sintatico = True
        else:
            print(
                "Erro sintatico - A declaracao do bloco de variáveis, mesmo que vazio, é obrigatória nessa linguagem - linha: " + self.linha_atual + "\n")
            self.arquivo_saida.write(
                "Erro sintatico - A declaracao do bloco de variáveis, mesmo que vazio, é obrigatória nessa linguagem - linha: " + self.linha_atual + "\n")
            print('Token problemático: ' + self.tokens[self.i])
            self.arquivo_saida.write('Token problemático: ' + self.tokens[self.i] + '\n')
            self.tem_erro_sintatico = True
        


