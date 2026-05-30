from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client_groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def obter_json(linha):
    resposta = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content":  
                        """
                            Você é um especialista em análise de dados e conversão de dados para JSON.
                            Você receberá uma linha de texto que é uma resenha de um aplicativo em marketplace online.
                            Eu quero que você analise esta resenha e me retorne um JSON com as seguintes chaves:
                            - 'usuario': o nome do usuário que fez a resenha
                            - 'resenha_original': a resenha no idioma original que você recebeu
                            - 'resenha_pt': a resenha traduzida para o português
                            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas estas três)

                            Exemplo de Entrada:
                            53409593$Safoan Riyad$J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.

                            Exemplo de Saída:
                            {
                                'usuario': 'Pedro Silva',
                                'resenha_original': 'This is a positive review for the app',
                                'resenha_pt': 'Esta é uma resenha positiva para o aplicativo',
                                'avaliacao': 'Positiva'
                            }

                            Regra importante: Você deve retornar APENAS o JSON, sem nenhum outro texto além do JSON.
                        """
            },
            {   
                "role": "user",
                "content": f"{linha}"
            }
        ],
        temperature=0
    )

    print(resposta.choices[0].message.content)
    return resposta.choices[0].message.content