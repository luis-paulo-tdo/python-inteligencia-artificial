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

### 2.7. Uso da Função Len
- Através dela, conseguimos obter o tamanho das listas de forma mais dinâmica e elegante.
- Podemos endereçar um número negativo para a lista e obter seus valores ao contrário.
- É possível particionar a lista passando dois endereços válidos entre o caractere `:`.
- Com a função `append(elemento)`, adicionamos um novo elemento dentro da lista.
- Com a função `extend(lista)` adicionamos os elementos de uma lista em outra lista.
- É possível também ter acesso a um elemento de uma lista dentro de outra lista.
- Através da função `remove(elemento)` conseguimos remover um elemento da lista.
- Através da função `pop()` conseguimos remover o último elemento dentro da lista.

### 2.8. Dicionários
- Em algumas situações, fica difícil trabalhar apenas com listas, aumentando o risco de erros.
- Na estrutura de Dicionário, temos a definição de chaves que são associadas a algum valor.
- Os valores dos dicionários podem ser acessados através de suas chaves entre colchetes.
- Os métodos `pop(chave)` e `get(chave)` também retornam os valores relacionados às chaves.
- Nos métodos `items()`, `keys()` e `values()`, recuperamos as chaves, valores ou ambos.

### 2.9. União de Dicionários
- Para termos uma estrutura com as chaves `nome` e `media`, podemos unir lista e dicionário.
- A lista, no caso, receberá dicionários cujas chaves são o `nome` e a `media` dos alunos.
- Cada dicionário, então, representará um aluno junto com a sua média correspondente.

## 3. Entrada e Conversão de Dados

### 3.1. Explorando o Loop For
- No For, sempre definimos quantas vezes as iterações ocorrerão dentro do laço.
- Podemos também definir uma lista que será iterada por meio de uma variável.
- A função `range(5)` retorna um array de números até o número cinco incluído.
- Podemos usar o `range(2, 7)` para definir o início e fim da lista numérica.
- Podemos usar `range(1, 10, 2)` para pular a lista de número em número.
- Ao passar um objeto no for, conseguimos iterar os dados dentro do objeto.
- Podemos iterar o `dicionario.items()` para obter chave e valor do objeto.
- Através do operador `%` (mod), conseguimos obter o resto de uma divisão.

### 3.2. Funções
- É uma forma de encapsular um bloco de código para que seja reutilizado mais de uma vez.
- As funçoes englobam ações para que possamos trabalhar com elas para diferentes valores.
- Utilizamos a palavra-chave `def` para declarar a função e definir os parâmetros dela.
- Através da função `split()`, conseguimos converter um texto em uma lista de palavras.
- Através da função `join()`, unimos os itens de uma lista definindo um separador.

### 3.3. Simplificação de Funções
- Conseguimos chamar uma cadeia inteira de funções para tratar um determinado valor.
- A exemplo, podemos corrigir uma string usando `" ".join(texto.upper().split())`.
- Para que seja possível usar funções em cadeia, elas precisam ter algum retorno.
- A função `random.choice(lista)` escolhe e retorna um elemento aleatório da lista.

### 3.4. Resumidor de E-mails
- Ao delimitar uma string com aspas triplas `"""` podemos adicionar quebras e identações nela.
- É possível combinar uma string contendo as aspas triplas com o `f` para interpolar valores.
- Se multiplicarmos uma string por um número N, iremos repetir esta string por N vezes.
- Através do método `enumerate(lista)`, conseguimos enumerar uma lista dentro do loop `for`.

### 3.5. LLMs Open Source
- O modelo do Gemini é privado, e por isso não conseguimos ver o que tem nele e baixá-lo.
- Existem modelos Open Source que permitem o download, o retreinamento e a privacidade.
- Dentre estes modelos, o Groq oferece um serviço de inferência para criadores de IA.
- Por meio do website do Groq, podemos realizar um cadastro e então gerar uma API Key.
- Com a API Key em mãos, conseguimos importá-la no Colab da mesma forma que o Gemini.
- Podemos escolher modelos diferentes, com maior ou menos raciocínio lógico, etc.
- Podemos definir por meio da `temperatura` o nível de criatividade da Inteligência.
- Quanto menor a temperatura, mais palavras prováveis ele utilizará nas inferências.
- Quanto maior a temperatura, mais palavras específicas serão escolhidas nas inferências.

## 4. Manipulação de Arquivos e Dados

### 4.1. Escrita de Arquivos
- Com a palavra-chave `with` e a função `open(arquivo, modo)` conseguimos criar um arquivo.
- Caso o modo inserido seja `w`, o arquivo é sempre sobrescrito pelo programa ao rodar.
- Se queremos adicionar novo conteúdo em vez de sobrescrever, usamos o modo `"w" x "a"`.
- Além disso, é importante que seja definido o encoding para o arquivo a ser escrito.
- Através da expressão `with as`, aplicamos o arquivo aberto a uma instância temporária.
- Através da instância, chamamos a função `write(conteudo)` para escrever uma linha.
- Com a função `writelines(lista)`, escrevemos uma lista inteira sem precisar iterar.

### 4.2. Leitura de Arquivos
- Na função `open(arquivo, modo)` passamos agora o modo `r` em vez do modo `w`.
- Com isso, iteramos a instância declarada para o arquivo para obter as linhas.
- Através da função `strip()` conseguimos tirar caracteres de quebra da linha.
- A função `readlines()` da instância do arquivo nos permite ler linha a linha.

### 4.3. O Framework Pandas
- Este framework é muito utilizado pela comunidade Python para ciência de dados.
- Este framework utiliza diferentes tipos de arquivos para manipulação de dados.
- A função `read_csv(caminho)` permite a leitura de um CSV no caminho passado.
- Ao ler o arquivo, seus dados são geralmente gravados em um `Data Frame`.
- A função `head(quantidade)` permite exibir os primeiros itens do frame.
- A função `tail(quantidade)` permite exibir os últimos itens do data frame.

### 4.4. Aplicando o Pandas
- A biblioteca `csv` nos permite escrever um CSV de forma segura a partir de uma lista objetos.
- Com o Data Frame do Pandas, conseguimos carregar um CSV a função `pd.DataFrame(arquivo)`.
- Podemos também transformar uma lista de objetos num arquivo CSV com a função `to_csv(lista)`.

## 5. Manipulação e Filtragem de Dados com Pandas

### 5.1. Manipulação de Dados
- A biblioteca `numpy` nos permite definir diferentes números aleatórios para dados mockados.
- Podemos imprimir apenas uma coluna do DataFrame referenciando `dataframe[nome_coluna]`.
- Conseguimos obter um array de valores únicos de uma coluna com a função `unique()`.
- A função `set(lista_colunas)` também nos permite pegar apenas os valores únicos.

### 5.2. Filtragem de Elementos
- Conseguimos fazer uma filtragem referenciando `dataframe[dataframe[coluna] == valor]`.
- Da mesma forma que aplicamos o `==`, podemos utilizar outros operadores de comparação.
- A propriedade `shape` de um Data Frame mostra os números de linhas e de colunas.
- Podemos combinar filtros com esta referência `dataframe[(filtro1) & (filtro2)]`.

### 5.3. Funções LOC e ILOC
- A propriedade `iloc[id]` nos permite trazer os detalhes de um item no Data Frame.
- Podemos exibir em intervalos finitos e infinitos com `iloc[id_inicio:id_fim]`.
- A propriedade `loc[índice]` obtém detalhes de um Data Frame indexado.
- Conseguimos retornar propriedades específicas com o `loc[índice, coluna]`.
- Múltiplos índices e colunas: `loc[[índice1, índice2], [coluna1, coluna2]]`.
- A propriedade `index` de uma filtragem traz a lista de índices do resultado.
- A lista de índices pode ser combinada: `df.loc[filtragem.index, colunas]`.
- Podemos alterar valores de uma coluna com `df.loc[índices, coluna] = valor`.

### 5.4. Criando Novas Colunas
- Para criar uma nova coluna, basta atribuir uma lista a uma propriedade do Data Frame.
- A referência é `df["propriedade"] = lista`, onde propriedade não pode existir ainda.
- Para apagar uma coluna, fazemos o uso de uma palavra-chave `del df["propriedade"]`.

# 6. Processamento com Inteligência Artificial

### 6.1. Tratamento de Erros
- Existem determinados blocos de códigos que sabemos que podem gerar algum erro.
- Para estes, não queremos a aplicação quebre e desejamos dar algum tratamento.
- Através do `try-except-finally`, podemos estruturar tratamentos de erro.
- Através do bloco `try`, realizamos a execução do bloco sujeito a erros.
- Através do `except`, especificamos um tipo de exceção e dar um tratamento.
- É uma boa prática criarmos nossas próprias exceptions para tratar os casos.
- Também existem exceções específicas já prontas para uso em erros esperados.
- Um `ValueError`, por exemplo, trata-se de problemas de conversão de dados.
- O `TypeError` geralmente se refere operações feitas com tipos diferentes.
- Com estas instâncias de exception, conseguimos obter mensagens específicas.
- Estas mensagens retornadas geralmente são próprias para os desenvolvedores.
- O tipo `Exception` é uma exceção genérica que pega qualquer erro gerado.
- O bloco `finally` serve para concluir o processamento da aplicação.
- Conclusões envolvem fechamento de arquivos, desalocações, etc.

### 6.2. Categorização de Dados
- Através da função `string.join(lista)` unimos diversas strings com um separador.
- Na função `string.split(separador)`, criamos uma lista de strings via separador.

### 6.3. Carregando Objetos JSON
- Através da biblioteca `json`, conseguimos trabalhar com serialização e desserialização.
- A função `json.loads(string)` nos permite converter uma string em um objeto JSON.
