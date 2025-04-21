# Suzano - Python Developer

Bem-vindo ao repositório do Bootcamp **Suzano - Python Developer**! Este espaço foi criado para consolidar os aprendizados e práticas realizadas durante o programa, abordando conceitos fundamentais e avançados de Python, incluindo tipagens, funções, Programação Orientada a Objetos (POO) e muito mais.

```markdown
> Este README foi escrito com a ajuda do GitHub Copilot, uma ferramenta de inteligência artificial que auxilia na criação de código e documentação de forma eficiente.
```

---

## Sobre o Bootcamp

O Bootcamp **Suzano - Python Developer** é uma iniciativa que visa capacitar desenvolvedores(as) com habilidades sólidas em Python, uma das linguagens de programação mais populares e versáteis do mercado. Durante o programa, exploramos desde os fundamentos da linguagem até conceitos avançados, preparando os participantes para desafios reais do mercado de trabalho.

---

## Conteúdo do Repositório

Este repositório contém exemplos, exercícios e anotações sobre os seguintes tópicos:

### 1. **Introdução ao Python**
- História e características da linguagem.
- Configuração do ambiente de desenvolvimento.
- Estrutura básica de um programa em Python.

### 2. **Tipagem em Python**
- Tipos de dados primitivos: `int`, `float`, `str`, `bool`.
- Estruturas de dados: `list`, `tuple`, `set`, `dict`.
- Tipagem dinâmica e estática.
- Uso de **type hints** com o módulo `typing`.

### 3. **Funções**
- Definição e uso de funções.
- Argumentos posicionais e nomeados.
- Funções com valores padrão.
- Funções anônimas (lambda).
- Decoradores e funções de ordem superior.

### 4. **Estruturas de Controle**
- Condicionais: `if`, `elif`, `else`.
- Laços de repetição: `for`, `while`.
- Compreensões de listas e dicionários.

### 5. **Programação Orientada a Objetos (POO)**
- Classes e objetos.
- Atributos e métodos.
- Encapsulamento, herança e polimorfismo.
- Métodos especiais (como `__init__`, `__str__`, etc.).
- Uso de classes abstratas e interfaces.

### 6. **Manipulação de Arquivos**
- Leitura e escrita de arquivos.
- Manipulação de arquivos CSV e JSON.
- Uso de bibliotecas como `pandas` para análise de dados.

### 7. **Tratamento de Exceções**
- Uso de `try`, `except`, `else` e `finally`.
- Criação de exceções personalizadas.

### 8. **Bibliotecas e Ferramentas**
- Introdução a bibliotecas populares como `numpy`, `pandas`, `matplotlib` e `requests`.
- Uso de ambientes virtuais com `venv` e `pipenv`.
- Gerenciamento de dependências com `pip`.

### 9. **Testes Automatizados**
- Introdução ao módulo `unittest`.
- Testes unitários e de integração.
- Uso de bibliotecas como `pytest`.

---

## Como Utilizar Este Repositório

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/suzano-python-developer.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd suzano-python-developer
    ```
3. Explore os arquivos e pastas para acessar os conteúdos de cada módulo.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novos conteúdos.

---

## Contato

Caso tenha dúvidas ou sugestões, entre em contato:
- **LinkedIn:** [Seu Nome]([https://www.linkedin.com/in/seu-perfil](https://www.linkedin.com/in/jonaslobo/))

---

# 🐍 Orientações sobre a Linguagem Python

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, conhecida por sua sintaxe simples e legibilidade. Abaixo estão algumas orientações importantes para quem está começando ou deseja aprimorar seus conhecimentos:

### 1. **Características Principais**
- **Fácil de aprender**: A sintaxe é intuitiva e próxima da linguagem natural.
- **Multiparadigma**: Suporta programação procedural, orientada a objetos e funcional.
- **Portabilidade**: Código Python pode ser executado em diferentes sistemas operacionais sem alterações.
- **Ampla comunidade**: Possui uma vasta comunidade de desenvolvedores e recursos disponíveis.

### 2. **Boas Práticas**
- **PEP 8**: Siga as diretrizes de estilo para escrever código limpo e legível.
- **Nomes descritivos**: Use nomes claros e significativos para variáveis, funções e classes.
- **Documentação**: Comente o código e utilize docstrings para explicar funcionalidades.
- **Evite repetições**: Aplique o princípio DRY (Don't Repeat Yourself) para evitar redundâncias.

### 3. **Gerenciamento de Dependências**
- Utilize ambientes virtuais (`venv`, `pipenv`) para isolar projetos e gerenciar bibliotecas.
- Liste as dependências no arquivo `requirements.txt` para facilitar a instalação.

### 4. **Depuração e Testes**
- Use o módulo `pdb` para depurar o código.
- Escreva testes automatizados para garantir a qualidade e funcionalidade do código.

### 5. **Performance**
- Prefira estruturas de dados nativas (`list`, `dict`, `set`) para operações rápidas.
- Utilize bibliotecas otimizadas como `numpy` para cálculos numéricos.
- Evite loops desnecessários e prefira compreensões de listas quando possível.

### 6. **Segurança**
- Valide entradas do usuário para evitar vulnerabilidades.
- Nunca exponha credenciais ou informações sensíveis no código.
- Utilize bibliotecas como `dotenv` para gerenciar variáveis de ambiente.

### 7. **Recursos de Aprendizado**
- Documentação oficial: [https://docs.python.org/](https://docs.python.org/)
- Cursos e tutoriais online.
- Fóruns e comunidades como Stack Overflow e Reddit.

Com essas orientações, você estará preparado para explorar e aproveitar ao máximo o potencial da linguagem Python!

### Exemplos de Código em Python

#### 1. **Função Complexa com Recursão**
```python
def fibonacci(n):
    """Calcula o n-ésimo número da sequência de Fibonacci."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Exemplo de uso
print(fibonacci(10))  # Saída: 55
```

#### 2. **Uso Correto da Sintaxe e Operadores**
```python
# Operadores aritméticos
a, b = 10, 3
print(a + b)  # Soma: 13
print(a - b)  # Subtração: 7
print(a * b)  # Multiplicação: 30
print(a / b)  # Divisão: 3.333...
print(a // b) # Divisão inteira: 3
print(a % b)  # Módulo: 1
print(a ** b) # Exponenciação: 1000

# Operadores lógicos
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

#### 3. **Função com Decorador**
```python
def log_decorator(func):
    """Decorador para registrar a execução de uma função."""
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com argumentos {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Resultado: {result}")
        return result
    return wrapper

@log_decorator
def soma(a, b):
    return a + b

# Exemplo de uso
soma(5, 7)
```

#### 4. **Dicas de Extensões para VSCode**
- **Python**: Suporte oficial para Python, incluindo linting, IntelliSense e depuração.
- **Pylance**: Fornece análise de tipo avançada e autocompletar.
- **Black Formatter**: Formata automaticamente o código seguindo o padrão PEP 8.
- **isort**: Organiza automaticamente as importações.
- **Jupyter**: Permite executar notebooks Jupyter diretamente no VSCode.
- **GitLens**: Integração avançada com Git para rastrear alterações no código.
- **Code Runner**: Executa scripts Python rapidamente no terminal.

#### 5. **Dica: Gerenciamento de Contexto**
```python
# Uso do gerenciador de contexto para manipulação de arquivos
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')

# O arquivo é fechado automaticamente ao sair do bloco "with"
```

#### 6. **Compreensão de Listas**
```python
# Criar uma lista de números pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

#### 7. **Uso de Bibliotecas Externas**
```python
import numpy as np

# Criar um array e calcular a média
dados = np.array([1, 2, 3, 4, 5])
media = np.mean(dados)
print(f"Média: {media}")  # Saída: Média: 3.0
```

Com esses exemplos e dicas, você pode aprimorar suas habilidades em Python e configurar seu ambiente de desenvolvimento de forma eficiente!
