#Declaração de variáveis
nomePrimeiraPessoa:str
nomeSegundaPessoa:str
idadePrimeiraPessoa:int
idadeSegundaPessoa:int

try:
    #Entrega de dados
    nomePrimeiraPessoa = input("Digite o nome da primeira pessoa")
    nomeSegundaPessoa = input("Digite o nome da segunda pessoa")
    idadePrimeiraPessoa = int(input("Digite a idade da primeira pessoa"))
    idadeSegundaPessoa = int(input("Digite a idade da segunda pessoa"))

    #Processamento de dados
    mediaDasIdades = (idadePrimeiraPessoa+idadeSegundaPessoa) / 2

    #Saída de dados
    print(f"A idade média de {nomePrimeiraPessoa} e {nomeSegundaPessoa} é {mediaDasIdades:.1f}")
except:
    print("Valor inválido, tente novamente")   




