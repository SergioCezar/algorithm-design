#Dupla Sertaneja: Sergio&Mateus; Mateus Scarpin Ribeiro (ra128459) e Sergio de Almeida Cezar (ra134680) 
import sys

def melhor_escolha(tempo_total: int, tarefas: list[tuple[int, int]]) -> int:
    # Ordena as tarefas por lucro decrescente
    tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: -tarefa[0])

    # Soma total de lucros possíveis (caso todas fossem realizadas)
    lucro_max = sum(lucro for lucro, _ in tarefas_ordenadas)
    lucro_obtido = 0  # Inicializa o lucro realmente obtido

    # Lista que controla o tempo disponível para agendamento
    proximo_livre = list(range(tempo_total + 1))

    # Tenta agendar as tarefas
    for lucro, prazo in tarefas_ordenadas:
        # Busca o tempo mais próximo livre antes do prazo
        tempo_disponivel = buscar_disponivel(proximo_livre, min(prazo, tempo_total))
        if tempo_disponivel > 0:
            # Ocupa o tempo encontrado
            ocupar_tempo(proximo_livre, tempo_disponivel, tempo_disponivel - 1)
            lucro_obtido += lucro  # Tarefa agendada

    # Retorna o prejuízo (lucro perdido)
    return lucro_max - lucro_obtido

# Função que encontra o tempo disponível usando union-find com compressão de caminho
def buscar_disponivel(proximo_livre, tempo):
    if proximo_livre[tempo] != tempo:
        proximo_livre[tempo] = buscar_disponivel(proximo_livre, proximo_livre[tempo])  # Compressão de caminho
    return proximo_livre[tempo]

# Atualiza o tempo ocupado, apontando para o próximo livre
def ocupar_tempo(proximo_livre, tempo_ocupado, novo_disponivel):
    proximo_livre[buscar_disponivel(proximo_livre, tempo_ocupado)] = buscar_disponivel(proximo_livre, novo_disponivel)

def main() -> None:
    input = sys.stdin.read
    linhas = input().splitlines()

    inputs = []
    aux = 0

    while aux < len(linhas):
        linha = linhas[aux].strip()
        if linha:
            n, h = map(int, linha.split())  
            tarefas = []
            for _ in range(n):
                aux += 1
                v, t = map(int, linhas[aux].strip().split())
                tarefas.append((v, t))  
            inputs.append((n, h, tarefas))  
        aux += 1

    for n, h, tarefas in inputs:
        resultado = melhor_escolha(h, tarefas)
        print(resultado)  

if __name__ == "__main__":
    main()
