'''
Nome: Andre Devay Torres Gomes
NUSP: 10770089

'''

# Função principal que roda a interface e chama as outras funções
def main():
    global solucao
    n = int(input('Digite o número N (entre 4 e 26) de rainhas que deseja no tabuleiro NxN :'))

    matriz = []
    solucao = []
    for i in range(n):
        matriz.append([' ']*(n))

    resposta(matriz, 0, n)
    print('-------------------------------------------------------------')
    print('Soluções em coordenadas de tabuleiro (de 1 a 26 e de A a Z):')
    print()
    print()

    for item in solucao:
        print (item)
        print()

    print("Total de soluções possíveis = {}".format(len(solucao)))


# Procura uma solução ao problema da N-Queens (usando recursividade)
def resposta(matriz, col, n):
    if col >= n:
        return
    
    for w in range(n):
        if checagem_espacos(matriz, w, col, n):
            matriz[w][col] = 1
            if col == n - 1:
                salvar(matriz)
                matriz[w][col] = 0
                return
            resposta(matriz, col + 1, n)
            matriz[w][col] = 0


# Confere se é possível colocar uma rainha em determinado espaço sem quebrar regras do jogo (chamada dentro de resposta() )
def checagem_espacos(matriz, lin, col, n):
    

    for colX in range(col):
        if matriz[lin][colX] == 1:
            return False
    
    linX = lin
    colX = col
    
    # Diagonal (1)
    while linX >= 0 and colX >= 0:
        if matriz[linX][colX] == 1:
            return False

        linX = linX - 1
        colX = colX - 1
    
    linS = lin
    colS = col
    
    # Diagonal (2)
    while linS < n and colS >= 0:
        if matriz[linS][colS] == 1:
            return False
        
        linS = linS + 1
        colS = colS - 1
    
    return True

# Converte 1 solução achada em coordenadas e, em seguida, a salva na lista de soluções
def salvar(matriz):
    global solucao

    conversao = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
     13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
    parcial = []
    cont1 = -1
    cont2 = -1

    for linha in matriz:
        cont1 = cont1 + 1
        for coluna in linha:
            cont2 = cont2 + 1
            if matriz[cont1][cont2] == 1:
                stringzando = str(cont2 + 1)
                ponto = conversao[cont1] + stringzando
                parcial.append(ponto)
        cont2 = -1    
    
    ' '.join(map(str, parcial))
    solucao.append(parcial)

main()