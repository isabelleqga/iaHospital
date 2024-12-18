import numpy as np
import random

# Parâmetros do problema
NUM_MEDICOS = 20
NUM_ENFERMEIROS = 30
TURNOS = ['manhã', 'tarde', 'noite']
DIAS_DA_SEMANA = 7
MIN_MEDICOS_POR_TURNO = 3
MIN_ENFERMEIROS_POR_TURNO = 5
LIMITE_HORAS_SEMANAIS = 40
CUSTO_HORA_EXTRA = 1.5

# Função para calcular o custo de uma solução
def calcular_custo(escala, preferencias, custos_horas_extra):
    custo = 0
    for profissional, turnos in escala.items():
        horas_totais = sum(turnos.values())
        if horas_totais > LIMITE_HORAS_SEMANAIS:
            custo += (horas_totais - LIMITE_HORAS_SEMANAIS) * CUSTO_HORA_EXTRA
        for turno, alocado in turnos.items():
            if alocado == 1 and turno in preferencias[profissional]:
                custo -= 1  # Penalidade negativa para satisfazer preferências
    return custo

# Função para verificar restrições
def verificar_restricoes(escala):
    for dia in range(DIAS_DA_SEMANA):
        for turno in TURNOS:
            medicos_alocados = sum(escala[f"medico_{i}"][f"{dia}_{turno}"] for i in range(NUM_MEDICOS))
            enfermeiros_alocados = sum(escala[f"enfermeiro_{i}"][f"{dia}_{turno}"] for i in range(NUM_ENFERMEIROS))
            if medicos_alocados < MIN_MEDICOS_POR_TURNO or enfermeiros_alocados < MIN_ENFERMEIROS_POR_TURNO:
                return False
    return True

# Função para gerar uma escala inicial
def gerar_escala_inicial():
    escala = {}
    for i in range(NUM_MEDICOS):
        escala[f"medico_{i}"] = {f"{dia}_{turno}": random.randint(0, 1) for dia in range(DIAS_DA_SEMANA) for turno in TURNOS}
    for i in range(NUM_ENFERMEIROS):
        escala[f"enfermeiro_{i}"] = {f"{dia}_{turno}": random.randint(0, 1) for dia in range(DIAS_DA_SEMANA) for turno in TURNOS}
    return escala

# Função para gerar uma escala vizinha
def gerar_escala_vizinha(escala):
    nova_escala = escala.copy()
    profissional = random.choice(list(nova_escala.keys()))
    turno = random.choice(list(nova_escala[profissional].keys()))
    nova_escala[profissional][turno] = 1 - nova_escala[profissional][turno]  # Troca entre 0 e 1
    return nova_escala

# Algoritmo Simulated Annealing
def simulated_annealing(preferencias, custos_horas_extra, temp_inicial=1000, taxa_resfriamento=0.99, iteracoes=1000):
    escala_atual = gerar_escala_inicial()
    custo_atual = calcular_custo(escala_atual, preferencias, custos_horas_extra)
    melhor_escala = escala_atual
    melhor_custo = custo_atual
    temperatura = temp_inicial

    for _ in range(iteracoes):
        vizinho = gerar_escala_vizinha(escala_atual)
        if not verificar_restricoes(vizinho):
            continue

        custo_vizinho = calcular_custo(vizinho, preferencias, custos_horas_extra)
        delta = custo_vizinho - custo_atual

        if delta < 0 or random.uniform(0, 1) < np.exp(-delta / temperatura):
            escala_atual = vizinho
            custo_atual = custo_vizinho

            if custo_vizinho < melhor_custo:
                melhor_escala = vizinho
                melhor_custo = custo_vizinho

        temperatura *= taxa_resfriamento

    return melhor_escala, melhor_custo

def formatar_melhor_escala(melhor_escala):
    for profissional, turnos in melhor_escala.items():
        print(f"\n{profissional.capitalize()}:")
        dias = {}
        for turno, valor in turnos.items():
            dia, periodo = turno.split("_")
            if dia not in dias:
                dias[dia] = {}
            dias[dia][periodo] = "X" if valor == 1 else " "
        
        print("Dia    Manhã  Tarde  Noite")
        print("-" * 25)
        for dia, periodos in sorted(dias.items()):
            print(f"{dia:<6} {periodos.get('manhã', ' '):<6} {periodos.get('tarde', ' '):<6} {periodos.get('noite', ' '):<6}")

# Definição das preferências e custos
preferencias = {f"medico_{i}": [f"0_manhã", f"1_tarde"] for i in range(NUM_MEDICOS)}
preferencias.update({f"enfermeiro_{i}": [f"2_noite", f"3_manhã"] for i in range(NUM_ENFERMEIROS)})
custos_horas_extra = {f"medico_{i}": CUSTO_HORA_EXTRA for i in range(NUM_MEDICOS)}
custos_horas_extra.update({f"enfermeiro_{i}": CUSTO_HORA_EXTRA for i in range(NUM_ENFERMEIROS)})

# Execução do algoritmo
melhor_escala, melhor_custo = simulated_annealing(preferencias, custos_horas_extra)

print("Melhor escala encontrada:")
formatar_melhor_escala(melhor_escala)
print(f"Custo total: {melhor_custo}")
