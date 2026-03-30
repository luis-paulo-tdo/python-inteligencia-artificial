# Python: Inteligência Artificial Aplicada 

## 1. Operações Básicas

### 1.1. Introdução e Configuração do Google Colab
- Com o Google Colab, podemos programar diretamente do navegador, sem precisar de uma máquina boa.

### 1.2. Explorando Células e a Função Print
- No Google Colab, podemos inserir textos e blocos de códigos que serão executados.
- A função `print("Valor")` permite exibir na tela algum valor.
- Porém, eu não consigo somar uma string com inteiro, preciso convertê-lo.

### 1.3. Variáveis e Concatenação de Strings
- É possível passar vários parâmetros para a função `print(valor1, valor2, valor3)`.
- Com isso, a string exibida separará os valores com o espaço.

### 1.4. Operações Matemáticas
- Dentro do Google Colab, precisamos reatualizar um total sempre que um dos seus fatores mudam.

### 1.5. Nomenclatura e Tipos de Dados
- Dentro do Python, a nomenclatura das variáveis é definida em `snake_case`.
- A função `type(variavel)` nos mostra o tipo de dado de uma variável.
- Os tipos primitivos das variáveis são: Int, Float, Str e Bool.

### 1.6. Manipulando Strings
- As funções `lower()` e `upper()` transformam a string em minúscula e maiúscula, respectivamente.
- A função `replace(elemento, substituto)` permite substituir um trecho de string por outro.
- A função `strip()` reduz espaços em excesso que possam vir junto com o valor das strings.

### 1.7. Recebendo Dados com Input e Formatando Textos com fStrings
- A função `input("Prompt: ")` permite que possamos inserir um dado de entrada para uma variável.
- Tudo o que iremos inserir através do `input` são de string, podendo precisar de conversão.
- A função `int(string)` nos ajuda a converter valores de string em números inteiros.
- A função `str(inteiro)` nos ajuda a converter valores de números inteiros em strings.
- Podemos fazer interpolação de strings usando a seguinte formatação `f"Idade: {idade}"`.

### 1.8. Condicionais
- As condicionais dentro do Python utilizam identação em vez de blocos delimitados por chaves.
- Na estrutura If-Else, há a palavra-chave `elif` que é uma simples abreviação de `else if`.
- O operador lógico `and` nos permite inserir mais premissas dentro de uma única condição. 

## 2. Manipulação de Strings

### 2.1. Conexão com Gemini
- A API Key deve ser gerado no Google AI Studio, logando na conta google e indo na tela adequada.
- Após obter a API Key que foi gerada, ela deve ser armazenada na Secrets do Google Colab.
- Em seguida, a API Key deve carregada via importação nas variáveis de ambiente do Python.
- Através da importação da biblioteca `genai`, conseguimos instanciar um cliente de IA.

### 2.2. Conceito de Loops
- Revisando a estrutura `while` dentro do Python no Google Colab, conhecimento básico.

### 2.3. Integração Dinâmica com Chatbots
- Conseguimos criar um chat com a Inteligência Artificial e armazenar dentro de uma variável.
- A partir desta variável, podemos chamar uma função de enviar mensagem com um prompt.
- A partir da propriedade `text`, conseguimos imprimir a resposta dada pela Inteligência.
- Conseguimos também obter o histórico de mensagens chamando a função `get_history()`.

### 2.4. Criando um Chatbot
- Através de um loop while, podemos fazer a captura de prompts, enviá-los ao chat e obter respostas.
- Enquanto a condição do loop não for atendida, novas perguntas podem ser feitas e respondidas.

### 2.5. Explorando Estrutura de Dados
- As listas armazenam um conjunto de valores do mesmo tipo e que podem ser acessadas via índice.

### 2.6. Desafio com Loop While
- Para percorrer uma lista de nome e uma lista de médias correspondentes ao nome, usamos um índice.
- O índice começa com zero, e enquanto ele for menor que o tamanho da lista, operamos os elementos.
- Somamos +1 para cada média percorrida na lista, e se o valor for maior que 10, ajustamos para 10.
- Então, imprimimos o nome do aluno e a sua média correspondente +1 ou 10 após o incremento feito.