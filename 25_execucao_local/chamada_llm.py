from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client_groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

resposta = client_groq.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "Olá! Você é um assistente de IA que responde sempre com um quote de uma unidade Starcraft 1, informando o nome da unidade como se fosse uma citação de livro."},
        {"role": "user", "content": "O que é uma IA Generativa?"}
    ],
    temperature=1.0
)

print(resposta.choices[0].message.content)