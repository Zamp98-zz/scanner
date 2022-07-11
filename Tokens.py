import re

relop = ['>', '<', '<=', '>=', '!=', '==', '!']
addop = ['+', '-']
comment = ['//', '/*', '*/']
reserved = ['main', 'return']
mulop = ['*', '/']
parenthesis = ['(', ')']
brackets = ['{','}']
memoryAddress = ['&', '[',']']
attrib = ['=']
type = ['int', 'float', 'void', 'double']
expression = [';']

tokens = {
    'relop' : relop,
    'addop' : addop,
    'type':type,
    'reserved' : reserved,
    'comment':comment,
    'mulop':mulop,
    'parenthesis':parenthesis,
    'brackets':brackets,
    'memoryAddress':memoryAddress,
    'attrib':attrib,
    'expression':expression
}

def cleanData(data):
    r=[]
    for line in data:
        temp = re.split('\n', line)
        for i in range(len(temp)):
            temp.remove('') if temp[i] == '' else temp[i]
        r.append(temp)
    return r

def getTokens(filename):
    try:
        linha = 1
        file = open(filename, 'r')
        data = file.readlines()
        cd = cleanData(data)
        t=[]
        for a in cd:
            for key in tokens:
                for k in tokens[key]:
                    print(a[0])
                    if a[0].find(k) != -1:
                        print("key",k,"found on", a)
                        t.append(key+'_'+k+'->'+str(linha)+'\n')
            linha += 1
        
        return t
    except:
        print("Erro")
