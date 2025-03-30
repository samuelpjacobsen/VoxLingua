# Documentação Linguística Acelerada com Machine Learning

Este projeto implementa um pipeline completo para acelerar a documentação de línguas usando técnicas de machine learning. O sistema é capaz de analisar arquivos de áudio para identificar padrões sonoros, estruturas linguísticas e produzir uma documentação inicial automática, que pode servir como ponto de partida para linguistas.

## 🎯 Principais Recursos

- Processamento automático de áudio multimodal
- Detecção de padrões sonoros (possíveis fonemas) via clustering não supervisionado
- Descoberta de estruturas linguísticas (palavras, morfologia, sintaxe)
- Geração de relatórios detalhados para análise
- Visualizações para facilitar a interpretação dos resultados

## 🚀 Começando

### Pré-requisitos

- Python 3.8+ 
- Conhecimentos básicos de linguística e processamento de áudio
- Arquivos de áudio de línguas que deseja documentar

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/samuelpjacobsen/VoxLingua.git
cd VoxLingua_repo
```

2. Instale o pacote em modo de desenvolvimento:
```bash
pip install -e .
```

3. Ou execute o script de configuração para instalar as dependências:
```bash
python setup.py install
```

4. Prepare seus dados de áudio em um diretório específico.

## 📊 Como Usar

### Processamento Básico de Áudio

```python
from voxlingua.audio.processor import AudioDocProcessor

# Inicializar o processador
processor = AudioDocProcessor()

# Analisar um arquivo de áudio
audio_path = "caminho/para/seu/audio.wav"
analysis = processor.analyze_segment(audio_path)

# Visualizar características
processor.visualize_features(analysis['features'])

# Ver transcrição automática (se o modelo reconhecer a língua)
print(analysis['transcription'])
```

### Descoberta de Padrões Sonoros

```python
from voxlingua.discovery.sound_patterns import SoundPatternDiscovery

# Inicializar a descoberta de padrões
discovery = SoundPatternDiscovery()

# Analisar um arquivo de áudio
audio_path = "caminho/para/seu/audio.wav"
results = discovery.analyze_sound_patterns(audio_path, n_clusters=8)

# Processar um diretório inteiro
audio_dir = "caminho/para/diretorio"
results_df, segments = discovery.process_directory(audio_dir, 
                                                output_csv="resultados_clusters.csv")
```

### Análise de Estruturas Linguísticas

```python
from voxlingua.discovery.language_structures import LanguageStructureDiscovery

# Inicializar a descoberta de estruturas
discovery = LanguageStructureDiscovery()

# Processar um diretório de áudios
audio_dir = "caminho/para/diretorio"
results = discovery.process_directory(audio_dir, 
                                    output_json="estruturas_linguisticas.json")

# Visualizar os resultados
discovery.visualize_language_patterns(results)
```

### Pipeline Completo

Para executar o pipeline completo de documentação em um diretório de áudios:

```bash
# Usando o script de linha de comando
voxlingua-pipeline --audio_dir caminho/para/diretorio --output_dir resultados

# Ou usando o script na pasta scripts
python scripts/process_audio.py --audio_dir caminho/para/diretorio --output_dir resultados
```

## 📝 Pipeline de Trabalho Recomendado

1. **Definição de Objetivos**: Comece delimitando exatamente o que deseja documentar (fonética, morfologia, sintaxe, etc.).

2. **Coleta de Dados**: Reúna arquivos de áudio da língua-alvo. Recomenda-se gravações em diferentes contextos, falantes e situações.

3. **Processamento Inicial**: Execute o pipeline em modo de teste com uma amostra pequena para verificar a qualidade dos resultados.

4. **Ajuste de Parâmetros**: Modifique os parâmetros (como número de clusters para fonemas) com base nos resultados iniciais.

5. **Processamento Completo**: Execute o pipeline completo em todos os dados e analise os resultados.

6. **Validação com Especialistas**: Trabalhe com linguistas para validar e refinar os resultados.

7. **Documentação Final**: Combine os insights automáticos com o conhecimento especialista para produzir a documentação.

## 🔍 Módulos Principais

### `voxlingua.audio.processor`

Contém a classe `AudioDocProcessor` para processamento básico de áudio, incluindo:
- Carregamento e normalização de áudio
- Extração de características (MFCC, pitch, energia)
- Transcrição automática (para línguas já modeladas)
- Visualização de características

### `voxlingua.discovery.sound_patterns`

Contém a classe `SoundPatternDiscovery` para descoberta de padrões sonoros:
- Segmentação automática de áudio
- Extração de características por segmento
- Agrupamento de segmentos semelhantes (potenciais fonemas)
- Visualização dos clusters

### `voxlingua.discovery.language_structures`

Contém a classe `LanguageStructureDiscovery` para análise de estruturas linguísticas:
- Descoberta de limites de palavras
- Análise de padrões sintáticos
- Descoberta de morfologia (prefixos, sufixos)
- Construção de redes de co-ocorrência de palavras

### `voxlingua.pipeline.documentation`

Pipeline completo que integra todos os módulos anteriores:
- Processamento de diretórios de áudio
- Geração de relatórios detalhados
- Visualizações para auxiliar na análise
- Exportação de resultados em formatos úteis

## 📈 Temas de Machine Learning Utilizados

1. **Aprendizado Não Supervisionado**
   - Algoritmos de clustering (K-means, DBSCAN)
   - Redução de dimensionalidade (PCA, t-SNE)
   - Detecção de padrões sem rótulos prévios

2. **Processamento de Linguagem Natural**
   - Análise de n-gramas para descoberta de palavras
   - Modelagem de co-ocorrência
   - Análise morfológica estatística

3. **Processamento de Áudio**
   - Extração de características acústicas (MFCC, F0)
   - Segmentação automática baseada em onsets
   - Reconhecimento automático de fala (wav2vec2)

4. **Transfer Learning**
   - Uso de modelos pré-treinados para iniciar a análise
   - Adaptação para novas línguas com dados limitados

5. **Redes e Grafos**
   - Modelagem de relações entre unidades linguísticas
   - Análise de comunidades em redes de palavras

## 🛣️ Próximos Passos

- Implementar visualizações interativas para análise mais detalhada
- Adicionar suporte para análise multimodal (vídeo + áudio)
- Integrar feedback de especialistas no pipeline
- Desenvolver modelos adaptativos que melhorem com o tempo
- Criar interface web para facilitar o uso por linguistas

## 📚 Referências e Recursos Adicionais

- [Documenting Endangered Languages with Linguist's Assistant](https://www.sil.org/resources/publications/entry/7874)
- [Low-Resource Speech Recognition](https://arxiv.org/abs/2008.13649)
- [Unsupervised Word Segmentation](https://aclanthology.org/P10-1040/)
- [Facebook AI wav2vec 2.0](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/)
- [Curso de Documentação Linguística (SOAS University of London)](https://www.soas.ac.uk/linguistics/research/research-clusters/documentation-and-description-of-endangered-languages/)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

---

Este projeto visa acelerar o processo de documentação linguística, mas não substitui o conhecimento especializado. Os resultados automáticos devem sempre ser validados por linguistas e falantes nativos das línguas documentadas.
