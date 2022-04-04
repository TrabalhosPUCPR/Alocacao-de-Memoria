import random as rdm

def deslocar(matriz, l, c, tam):
    for y in range(c, len(matriz)):
      for x in range(l, len(matriz[y])):
        matriz[y][x] = 0
        tam -= 1
        if tam == 0:
          return matriz
  
def divisa():
    print("-"*120+"\n"+"-"*120)

def criar_matriz(colunas, linhas, chance = 50, local=False):
    matriz = []
    coord = []
    for y in range(linhas):
        matriz.append([])
        for x in range(colunas):
            if rdm.randint(0, 100) <= chance:
                coord.append(((x/2)+1, y))
                matriz[y].append(1)
            else:
                matriz[y].append(0)
    if local == False:
        return matriz
    else:
        return matriz, coord

def printMatriz(matriz):
    try:
        for y in range(len(matriz)):
            for x in range(len(matriz[y])):
                print("|", end="")
                if matriz[y][x] != 0:
                    print("X", end="")
                else:
                    print(" ", end="")
            print("|")
    except:
        print("Insira uma matriz válida")

def aloc_firstfit(matriz, tam):
    cont = []
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if matriz[y][x] == 0:
                cont.append([x, y])
            else:
                cont = []
            if len(cont) == tam:
                for y in range(len(cont)):
                    matriz[cont[y][1]][cont[y][0]] = 1                       
                return matriz
    print("Não há espaço na memória da matriz")

def aloc_bestfit(matriz, tam):
    cont = []
    best = None
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if matriz[y][x] == 0:
                cont.append([x, y])
            else:
                cont = []
            if len(cont) >= tam:
                if best == None:
                    best = cont
                elif len(cont) < len(best):
                    best = cont
    if best == None:
        print("Nao ha espaco na matriz")
    else:
        for y in range(tam):
            matriz[best[y][1]][best[y][0]] = 1                       
        return matriz

def aloc_worstfit(matriz, tam):
    cont = []
    best = None
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if matriz[y][x] == 0:
                cont.append([x, y])
            else:
                cont = []
            if len(cont) >= tam:
                if best == None:
                    best = cont
                elif len(cont) > len(best):
                    best = cont
    if best == None:
        print("Não ha espaco na matriz")
    else:
        for y in range(tam):
            matriz[best[y][1]][best[y][0]] = 1                       
        return matriz

while True: 
  coluna = int(input("Digite a quantidade de colunas\n>> "))
  linha = int(input("Digite a quantidade de linhas\n>> "))

  if coluna <= 0 or linha <= 0:
        print("\nNúmero inválido\n")
  else: break

matriz=criar_matriz(coluna,linha)

divisa()

while True:

    escolha = int(input('1-Escolher um espaço para a alocação \n2-Mostrar memória \n>>'))

    divisa()

    if escolha == 1:
     printMatriz(matriz)
     
     divisa()

     escolha2=int(input('Dessas possíveis escolhas qual o úsuario deseja usar?\n1-First fit\n2-Best fit\n3-Worst fit\n4-Deslocação\n5-Visualizar \n>>'))
     

     divisa()

     if escolha2==1:
      tam = int(input('Quantos espaços serão alocados? \n>> '))
      aloc_firstfit(matriz,tam)
      divisa()
      printMatriz(matriz)

     elif escolha2==2:
      tam = int(input('Quantos espaços serão alocados? \n>> '))
      printMatriz(aloc_bestfit(matriz, tam))

     elif escolha2 == 3:
        tam = int(input('Quantos espaços serão alocados? \n>> '))
        printMatriz(aloc_worstfit(matriz, tam))

     elif escolha2 == 4:
        x1= int(input('Coluna que a deslocacao iniciara\n>>'))
        y1 = int(input('Linha que a deslocacao iniciara\n>>'))
        tam = int(input('Digite o tamanho da deslocacao\n>>'))
         
        matriz = deslocar(matriz, y1, x1, tam)
        divisa()

     elif escolha2 == 5:
        printMatriz(matriz)
      

    elif escolha == 2:   
     printMatriz(matriz)




