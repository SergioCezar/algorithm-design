#Dupla Sertaneja: Sergio&Mateus; Mateus Scarpin Ribeiro (ra128459) e Sergio de Almeida Cezar (ra134680) 
import sys

def efeito_domino(N, H, D):
    # Calcula a posição cumulativa de cada peça ao longo da linha
    x = [0] * N
    for i in range(1, N):
        x[i] = x[i-1] + D[i-1]
        
    # dp[i]: o maior número de peças que podem ser mantidas no lugar até a peça i
    dp = [float('-inf')] * N
    dp[0] = 1  # Sempre mantemos a primeira peça fixa
    
    # Para cada peça i, tentamos estender a melhor solução de alguma peça anterior j
    for i in range(1, N):
        for j in range(0, i):
            # Verifica se o segmento de j até i respeita o limite de altura
            if x[i] - x[j] <= (i - j) * H:
                # Se for possível, atualiza dp[i] se encontrarmos um caminho melhor
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                
        # Se nenhuma transição foi válida, marcamos dp[i] como inalcançável
        if dp[i] < 1:
            dp[i] = float('-inf')
            
    # Verifica se a última peça pode ser alcançada mantendo ao menos a primeira e a última fixas
    if dp[N-1] < 2:
        return -1
    else:
        # O número de peças removidas é o total menos o número de peças mantidas
        return N - dp[N-1]

def main():
    data = sys.stdin.read().split()
    index = 0
    results = []
    
    while index < len(data):
        N = int(data[index])
        H = int(data[index + 1])
        index += 2
        
        if N == -1 and H == -1:
            break
        
        D = list(map(int, data[index : index + N - 1]))
        index += N - 1
        
        resultado_caso = efeito_domino(N, H, D)
        results.append(str(resultado_caso))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
