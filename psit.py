import unicodedata

from numpy import append
"""
Importação da unicodedata para desenvolvimento da função de tratamento de nomes.
"""

class Pessoa:
    def __init__(self, nome, cpf, entidade, bolsa, ano):
        self.nome = nome 
        self.cpf = cpf
        self.entidade = entidade
        self.bolsa = bolsa
        self.ano = ano
"""
Classe que tem recebes os atributos: nome, cpf, entidade de ensino, valor da bolsa e ano, 
de cada indivíduo da base de dados.
"""

def tratador_nome(nome: str)-> str:
    normalizada = unicodedata.normalize('NFD', nome)
    return ''.join([letter for letter in normalizada if not unicodedata.combining(letter)]).casefold()
"""
Função que realiza o tratamento de nomes,tirar acentos e deixar as letras minúsculas, baseada na resolução de 
Luciano Ramalho em seu livro "Python Fluente".
"""

def ano_existe(anosNovo,existe,ano)->bool:
    for t in range(len(anosNovo)):
        if(ano == anosNovo[t]):
            existe = True
    return existe
"""
Função que faz a consistência se o ano procurado existe na base de dados.
Utilizada para anos que utilizam, como entrada, um ano procurado.
"""

def lista_ranking(pessoas,lista):
    iterativa = 0
    for x in range(len(pessoas)):
        if(iterativa<3):
            if(float(pessoas[x].bolsa)==lista[iterativa]):
                print('Nome: '+ pessoas[x].nome + '; CPF: '+ pessoas[x].cpf + '; Valor da Bolsa: R$'+ pessoas[x].bolsa +'\n')
                iterativa+=1
"""
Função que lista o top 3 de pessoas baseando-se no seu valor de bolsa. 
Funciona para procurar o top 3 de uma lista crescente ou decrescente de valores
"""
def funcao1(anosNovo,pessoas):
    existe = False
    while(existe == False):
        ano = input('\nInsira o ano desejado:\n')
        existe = ano_existe(anosNovo,existe,ano)
        if(existe):
            verifica_presença = False
            for t in range(len(anosNovo)):
                if(ano == anosNovo[t]):
                    i=0
                    while(verifica_presença!=True):
                        if(pessoas[i].ano == anosNovo[t]):
                            print('Nome:'+ pessoas[i].nome + ';' + 'CPF:' + pessoas[i].cpf + ';' + 'Entidade:' + pessoas[i].entidade + ';' + 'Valor da Bolsa: R$' + pessoas[i].bolsa + '\n')
                            verifica_presença = True
                        i+=1
                    verifica_presença = False
        else:
            print('Ano inválido!')
"""
Função para a primeira funcionalidade. Primeiramente, faz o pedido do ano desejado e depois sua consistência.
Então realiza a procura do indivíduo zero para aquele ano dentro de uma lista pessoas.
"""

def funcao2(pessoas):
    codificado = [] 
    encontrado = False
    procurado = input('\nInsira o nome procurado:')
    procurado = tratador_nome(procurado)
    procurado = procurado.split(' ')
    for t in range(len(pessoas)):
        comparado = tratador_nome(pessoas[t].nome)
        comparado = comparado.split(' ')
        for k in range(len(procurado)):
            if(procurado[k]==comparado[k]):
                encontrado = True
            else:
                encontrado = False
                break
        if(encontrado==True):
            procurado = comparado
            for palavra in procurado:
                palavra = list(palavra)
                segura = palavra[0]
                palavra[0] = palavra[-1]
                palavra[-1] = segura
                palavra = palavra[::-1]
                for k in range(len(palavra)):
                    if(ord(palavra[k])+1>ord('z')):
                        palavra[k]=str(chr(ord(palavra[k])-25))
                    else:  
                        palavra[k]=str(chr(ord(palavra[k])+1))
                palavra = "".join(palavra)
                palavra = palavra.upper() 
                codificado.append(palavra)
                codificado.append(' ')
            codificado = "".join(codificado)
            print('Nome: ' + codificado + ';' + ' Ano:' + pessoas[t].ano + ';' + ' Entidade:' + pessoas[t].entidade + ';' + ' Valor da Bolsa: R$' + pessoas[t].bolsa + '\n')
            break
    if(encontrado==False):
        print('Nome não encontrado!')
"""
Função implementada para a funcionalidade 2. Primeiramente, pede um nome de uma pessoa, seja seu nome completo ou parcial.
Depois é feito o tratamento dessa entrada tirando acentos e tornando as letras maiúsculas, e separação do nome baseando-se
em um espaço vazio para a formação de uma array de nomes. Então, é feito um loop interativo e, para cada iteração,
obtem-se um nome de pessoa a partir de uma lista. Esse nome recebe o mesmo tratamento que o nome de entrada recebeu. Após
isso, então é feito a comparação de cada posição da array de entrada e da array obtida da lista de dados, se, quando a 
array de entrada acabar, todos as partes forem iguais, significa que a pessoa foi encontrada e então faz-se a codificação
do nome, no caso, o nome completo. Essa codificação é feita em cada pedaçodo nome completo. Para o nome "maria", por exemplo
faz se a troca da primeira letra com a segunda, aarim, depois a inversão total das letras, miraa, depois cada letra é trocada
por seu sucessor na ordem alfabética, njsbb, essa troca pelo sucessor é baseada no código ascii de cada letra pegando o seu
código + 1 e, no caso da letra z, faz-se código - 25. Para finalizar as novas palavras tem suas letras transformadas em 
maiúsculas e as palavras são juntadas formando o nome completo que, então, é disposto na tela juntamente com outras informações
sobre o indivíduo obtidas da mesma lista de pessoas, que contém suas informações. Se o nome não for encontrado ele emite um 
aviso informando.
"""

def funcao3(anosNovo,medias):
    existe = False
    while(existe == False):
        ano = input('\nInsira o ano desejado:\n')
        existe = ano_existe(anosNovo,existe,ano)
        if(existe):
            for t in range(len(medias)):
                if(medias[t][0]==ano):
                    print('Média anual: R$',round(medias[t][1],2),'\n')
        else:
            print('Ano inválido!')
"""
Função implementada para funcionalidade 3. Primeiramente, faz o pedido do ano desejado e depois sua consistência.
Então, para cada indivíduo com ano corresponde, o valor de sua bolsa é adicionado a uma variável acumulativa e um contador de pessoas
é incrementado. Depois, é feita a média anual. 
"""

def funcao4(pessoas,lista_decrescente,lista_crescente):
   
    print('\nTop 3 maiores bolsas:\n')
    lista_ranking(pessoas,lista_decrescente)
   
    print('\nTop 3 menores bolsas:\n')
    lista_ranking(pessoas,lista_crescente)
"""
Função implementada para funcionalidade 4. A partir de uma lista de informações de pessoas são retirados valores de bolsas
e colocados em uma lista de valores. Tal lista é organizada com a função sorted de forma crescente e decrescente sendo criadas
duas novas listas. Então, a função de listar um ranking, top 3, é chamada passando como parâmetro as duas novas listas e as 
informações são dispostas na tela.
"""
    
def main():
    anos = []
    #array que guarda todos os anos presentes na base de dados, com cópias.
    anosNovo = []
    #array que guarda todos os anos presentes na base de dados, mas sem cópias.
    pessoas = []
    #array que guarda varios objetos da classe Pessoa.

    f = open("br-capes-bolsistas-uab.csv","r", encoding='utf8', errors='ignore')
    lines = f.readlines()
    #leitura do arquivo da base de dados

    for line in lines[1:]:
        line = line.split(';')
        anos.append(line[4])
        identifica = Pessoa(line[0],line[1],line[2],line[10][:-1],line[4])
        pessoas.append(identifica)
    #para cada linha do banco de dados é preenchida a lista de pessoas com as informações de interesse.

    verifica_presença = True
    anosNovo.append(anos[0])
    for t in range(len(anos)):
        for x in range(len(anosNovo)):
            if(anos[t]==anosNovo[x]):
                verifica_presença = False        
        if(verifica_presença):
            anosNovo.append(anos[t])
        verifica_presença = True 
    #a partir da lista com todos os anos, incluindo cópias, é feita uma lista nova, mas sem cópias. 


    medias = []
    #lista que salva em cada posição uma outra lista que contém dois elementos.
    #o primeiro: um ano; o segundo: a media do valor de bolsa do respectivo ano.
    soma_valores = 0
    total_pessoas=0
    for t in range(len(anosNovo)):
        segura = []
        #lista que guarda um ano e sua media anual de valor de bolsa.
        #essa lista é guardada dentro da lista 'medias' e a cada iteração é zerada.
        soma_valores = 0
        total_pessoas = 0
        segura.append(anosNovo[t])
        for i in range(len(pessoas)):
            if(pessoas[i].ano == anosNovo[t]):
                soma_valores += float(pessoas[i].bolsa)
                total_pessoas += 1 
        media=float(soma_valores/total_pessoas)
        segura.append(media)
        medias.append(segura)


    lista_valores = []
    #lista com valores de bolsas
    
    for x in range(len(pessoas)):
        lista_valores.append(float(pessoas[x].bolsa))
    lista_crescente = sorted(lista_valores, reverse = False)
    lista_decrescente = sorted(lista_valores, reverse = True) 
    
    opcao=0
    while(opcao!=5):
        opcao = int(input('Selecione sua opção:\n1-Consultar bolsa zero\n2-Codificar nomes\n3-Consultar a média anual\n4-Ranking de valores de bolsas\n5-Terminar programa\nOpção:'))
        if((opcao==1)or(opcao==2)or(opcao==3)or(opcao==4)or(opcao==5)):
            if(opcao == 1):
                funcao1(anosNovo,pessoas)
            elif(opcao==2):
                funcao2(pessoas)
            elif(opcao==3):
                funcao3(anosNovo,medias)
            elif(opcao==4):
                funcao4(pessoas,lista_decrescente,lista_crescente)
            else:
                break
        else:
            print('Opção inválida! Escolha outra')
    #Interface de console, pede a opção de escolha, caso seja inválida pede por outra.
   
if __name__ == "__main__":
    main()
   
    