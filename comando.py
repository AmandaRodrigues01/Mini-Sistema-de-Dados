def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro!! Por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
     
        else:    
            return n 
def linha(tam=42):
    return '-' * tam
    

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('\033[34mMENU PRINCIPAL\033[m')
    c =0
    for item in lista:
        c  +=1
        print(f'\033[34m{c} -> {item}\033[m')
    print(linha())
    opc = leiaInt('\033[33mDigite Sua Opção:\033[m')
    return (opc)
