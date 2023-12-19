from comando import cabeçalho
def documento(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        
        for linha in a:
            linha.split(':')
            print(linha)
        
            
            # dado = linha.split(';')
            # dado[1]= dado[1].replace('\n','')
            # print(f'{dado[0]:30} {dado[1] :>3} anos')           
    finally:
        a.close()
def escrever(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq,'at')
        
    except:
        print('Erro ao ler o arquivo')
    else:
        try:
           
            a.write(f'\n{nome:<30}{idade:>3} anos\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'\033[36mNovo cadastro de {nome} com sucesso\033[m')
        a.close()