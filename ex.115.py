from comando import menu 
import  comando 
from arquivo import escrever
from arquivo import documento
from arquivo import criarArquivo
from arquivo import lerArquivo
from comando import leiaInt
from arquivo import escrever
arq = 'texto.txt'
if not documento(arq):
    
    criarArquivo(arq)
# comando.cabeçalho('menu principal ')
while True:
    resposta=menu(['\033[34mMostrar Pessoas Cadastradas','Cadastrar Pessoas','Sair do Programa\033[m'])
    # resposta = int(input('\033[33mdigite sua opção: \033[m'))
  
    if resposta == 1:
    
       lerArquivo(arq)
    if resposta ==2:
       print('NOVO CADASTRO')
       
       nome = str(input('nome:'))
       idade = leiaInt('idade')
       escrever(arq,nome,idade)
    if resposta == 3:
        print('\033[34mfim do sistema\033[m')
        break
    if resposta >3:
        print('\033[31mErro!Valor inválido,digite uma das opções.\033[m')
        continue 
