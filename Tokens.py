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
    'reserved' : reserved,
    'comment':comment,
    'mulop':mulop,
    'parenthesis':parenthesis,
    'brackets':brackets,
    'memoryAddress':memoryAddress,
    'attrib':attrib,
    'type':type,
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
        file = open(filename, 'r')
        data = file.readlines()
        cd = cleanData(data)
        t=[]
        for a in cd:
            for key in tokens:
                for k in tokens[key]:
                    if a[0].find(k) != -1:
                        print("key",k,"found on", a)
                        t.append({key: k})
        print(t)

    except:
        print("Erro")
