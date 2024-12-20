# Agendamento de Profissionais de Saúde com Simulated Annealing

## Descrição

Este projeto utiliza o algoritmo de *Simulated Annealing* para encontrar uma solução otimizada de escalas de trabalho para médicos e enfermeiros em um hospital. A solução leva em consideração as preferências de turno de cada profissional, limitações de horas semanais e as exigências mínimas de profissionais por turno, buscando minimizar custos extras com horas trabalhadas além do limite.

## Requisitos

- Python 3.x
- Pacotes:
  - `numpy` (para cálculos de temperatura e funções matemáticas)
  - `random` (para geração de números aleatórios)

Você pode instalar o pacote `numpy` com o seguinte comando:

```bash
pip install numpy
```

## Estrutura do Código

### Parâmetros do Problema

- **NUM_MEDICOS**: Número total de médicos.
- **NUM_ENFERMEIROS**: Número total de enfermeiros.
- **TURNOS**: Lista de turnos disponíveis: manhã, tarde, noite.
- **DIAS_DA_SEMANA**: Número de dias para agendamento (7 dias).
- **MIN_MEDICOS_POR_TURNO**: Mínimo de médicos por turno.
- **MIN_ENFERMEIROS_POR_TURNO**: Mínimo de enfermeiros por turno.
- **LIMITE_HORAS_SEMANAIS**: Limite de horas semanais para cada profissional (40 horas).
- **CUSTO_HORA_EXTRA**: Fator de custo adicional para horas extras (1.5x).

### Funções Principais

1. **`calcular_custo`**: Calcula o custo de uma solução baseada em turnos alocados, considerando horas extras e preferências.
2. **`verificar_restricoes`**: Verifica se a escala proposta atende às restrições de número mínimo de profissionais por turno.
3. **`gerar_escala_inicial`**: Gera uma escala inicial aleatória.
4. **`gerar_escala_vizinha`**: Gera uma nova escala aleatória próxima da solução atual para o algoritmo de *Simulated Annealing*.
5. **`simulated_annealing`**: Implementa o algoritmo de *Simulated Annealing* para encontrar a melhor escala de trabalho.
6. **`formatar_melhor_escala`**: Formata e imprime a melhor escala encontrada pelo algoritmo.

## Como Executar

1. **Baixe o arquivo**:

   Se você não tiver o código localmente, baixe o arquivo anexado chamado "app.py" e navegue até o diretório que ele está.

2. **Instale os requisitos**:

   Se você ainda não tem o `numpy`, instale-o com:

   ```bash
   pip install numpy
   ```

3. **Execute o código**:

   Execute o script Python contendo o algoritmo com o seguinte comando:

   ```bash
   python app.py
   ```

   Onde `app.py` é o nome do seu arquivo Python. O script irá rodar o algoritmo de *Simulated Annealing* e imprimir a melhor escala encontrada, juntamente com o custo total da solução.

## Personalização

- **Preferências dos Profissionais**: No código, as preferências de cada profissional são definidas nas variáveis `preferencias` e podem ser modificadas conforme necessário. Por exemplo, se um médico preferir trabalhar no turno da noite, você pode ajustar a lista de turnos para esse profissional.

- **Custos das Horas Extras**: O valor de `CUSTO_HORA_EXTRA` pode ser alterado para ajustar o custo extra de horas trabalhadas além do limite de 40 horas semanais.

## Exemplo de Saída

A execução do código produzirá uma saída formatada da escala de trabalho, como mostrado abaixo:

```plaintext
Melhor escala encontrada:

medico_0:
Dia    Manhã  Tarde  Noite
-------------------------
0      X      X      X     
1      X      X      X     
2      X      X      X     
...

Custo total: 30.5
```

Onde "X" indica que o profissional está alocado para aquele turno.
