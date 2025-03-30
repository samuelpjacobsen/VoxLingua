# Título da Issue: Implementar distinção entre fones e fonemas

## Descrição
Na linguística existe uma diferença crucial entre fone e fonema:

- **Fones**: são todos os sons que são pronunciados em uma língua.
- **Fonemas**: são os sons que, quando substituídos, mudam o sentido de uma palavra.

Podemos ter diferentes fones que não alteram o sentido da palavra (alofones).

## Contexto adicional
O teste para descobrir se um som é um fonema é comparar palavras com fones pares (pares mínimos) e verificar se a substituição altera o significado.

Por exemplo:
- "pata" e "bata" em português: a substituição de /p/ por /b/ muda o significado, logo /p/ e /b/ são fonemas distintos.
- Mas certas variações do som /r/ em português não alteram o significado das palavras, logo são alofones e não fonemas distintos.

## Solução proposta
1. Implementar detecção e classificação de fones
2. Implementar comparação de pares mínimos
3. Desenvolver algoritmo para identificar fonemas com base em significado
4. Atualizar o modelo de ML para distinguir entre fones e fonemas

## Tarefas
- [ ] Criar módulo para distinção fonema/fone
- [ ] Implementar algoritmo de detecção de pares mínimos
- [ ] Desenvolver sistema para análise contrastiva
- [ ] Integrar com o pipeline de documentação linguística
