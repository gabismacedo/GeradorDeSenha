# Gerador de Senha Automático

Este projeto é uma aplicação simples em Flask que gera tokens/senhas aleatórias.

## Estrutura do projeto

- `gerar_senha.py`
- `main.py`
- `routes.py`
- `templates/index.html`

## O que cada arquivo faz

### `gerar_senha.py`
Contém a lógica de geração de senha.

- Importa `secrets` e `string` para criar uma senha segura.
- Cria um conjunto de caracteres válidos usando letras maiúsculas e minúsculas e dígitos.
- Remove alguns caracteres especiais indesejados da lista (`%&'()+,-./:;<=>[\]^_`{|}~`).
- Gera um token de tamanho definido pelo usuário (padrão 12) usando `secrets.choice`.
- Retorna o token gerado.

### `main.py`
É o ponto de entrada da aplicação Flask.

- Importa a função `gerar_senha` de `gerar_senha.py`.
- Cria a instância `app` do Flask.
- Importa todas as rotas de `routes.py`.
- Executa o servidor Flask quando o script é iniciado diretamente.

### `routes.py`
Define a rota principal da aplicação.

- Importa o app Flask de `main.py` e a função `gerar_senha`.
- Usa `request` e `render_template` do Flask.
- Define a rota `/` aceitando métodos `GET` e `POST`.
- No `GET`, exibe o formulário vazio.
- No `POST`, lê o valor `qtd` do formulário, valida e converte para inteiro.
- Ajusta a quantidade para valores válidos:
  - valor menor que 1 => 12
  - valor maior que 30 => 20
  - valor inválido => 12
- Gera o token e renderiza a página `index.html` com o resultado.

### `templates/index.html`
Página HTML que exibe o formulário e o token gerado.

- Contém um formulário com campo para a quantidade de caracteres.
- Envia os dados usando `POST`.
- Mostra o token gerado quando ele está disponível.

## Como executar

1. Instale o Flask (se ainda não estiver instalado):

```bash
pip install flask
```

2. Execute a aplicação:

```bash
python main.py
```

3. Abra o navegador em `http://127.0.0.1:5000/`.

## Observações

- O valor mínimo de caracteres no formulário é `12` e o máximo é `30`.
- Se o valor enviado for inválido, o sistema usa `12` como padrão.
- A geração de senha evita caracteres especiais que podem ser problemáticos em alguns contextos.