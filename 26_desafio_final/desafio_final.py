from funcoes_llm import obter_json
from funcoes_processamento import obter_consolidacao
import json

resenhas = []
objetos_resenha = []

# Etapa 1 - Armazenando conteúdo do arquivo em uma lista

print("[1] Carregando resenhas do arquivo")

with open("resenhas-app-gpt.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        resenhas.append(linha.strip())


# Etapa 2 - Transcrevendo para JSON usando um LLM

print("[2] Transcrevendo lista de resenhas para JSON")

for resenha in resenhas:
    string_resenha = obter_json(resenha)
    objeto_resenha = json.loads(string_resenha)
    objetos_resenha.append(objeto_resenha)

print("[3] Obtendo consolidação das resenhas")

comentarios, positivos, negativos, neutros = obter_consolidacao(objetos_resenha)

print(f"Resenhas Positivas: {positivos}")
print(f"Resenhas Negativas: {negativos}")
print(f"Resenhas Neutras: {neutros}")
print(f"Comentários Consolidados: {comentarios}")
