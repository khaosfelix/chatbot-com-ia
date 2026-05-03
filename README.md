# Chatbot com IA

> Aplicação web em Python com Streamlit e OpenAI API para criação de chatbot com interface personalizada, histórico de conversa e estilização própria.

## Visão geral

Este projeto foi desenvolvido para praticar a construção de aplicações web em Python, integração com API e personalização de interface com foco em experiência do usuário.

A aplicação permite que o usuário envie mensagens em um chat, acompanhe o histórico da conversa em tempo real e receba respostas geradas por IA em uma interface visual autoral, com estética dark e apresentação mais marcante.

Mais do que um exercício técnico, este projeto também explora a combinação entre funcionalidade, identidade visual e organização de código, mostrando como uma aplicação simples pode ganhar mais presença quando há cuidado com usabilidade e apresentação.

## Principais funcionalidades

- Interface web construída com Streamlit
- Campo de mensagem com `st.chat_input`
- Exibição de mensagens com `st.chat_message`
- Histórico da conversa salvo em `st.session_state`
- Integração com a API da OpenAI
- Botão para limpar a conversa
- Estilização personalizada com CSS dentro do Streamlit

## Demonstração

Em breve: print da interface e/ou link da aplicação publicada.

## Cuidados de segurança

A chave da API deve ser armazenada em `.streamlit/secrets.toml` e nunca publicada no GitHub. 

## Tecnologias utilizadas

- Python
- Streamlit
- OpenAI API
- CSS customizado

## Estrutura do projeto

```bash
chatbot-com-ia/
├── main.py
├── apoio.py
├── README.md
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

## Como executar o projeto

1. Clone este repositório ou baixe os arquivos
2. Abra a pasta no VS Code
3. Instale as dependências
4. Configure sua chave da OpenAI
5. Rode o projeto com Streamlit

## Instalação das dependências

```bash
pip install -r requirements.txt
```

## Configurando a chave da API

Crie uma pasta chamada `.streamlit` na raiz do projeto.

Depois, dentro dela, crie um arquivo chamado `secrets.toml` com este conteúdo:

```toml
OPENAI_API_KEY = "sua-chave-aqui"
```

Esse arquivo não deve ser enviado para o GitHub.

## Executando a aplicação

```bash
streamlit run main.py
```

## O que este projeto demonstra

Este projeto evidencia, na prática:

- criação de aplicações web com Python
- integração com API
- gerenciamento de estado com `session_state`
- construção de interface conversacional
- personalização visual com CSS
- organização de projeto para portfólio no GitHub

Além da parte técnica, ele também reforça um ponto importante do meu processo de transição para tecnologia: o interesse em construir soluções que unam lógica, clareza, experiência do usuário e identidade visual.

## Próximos passos

Algumas evoluções possíveis para este projeto:

- escolha de modelo pela interface
- tratamento de erros da API
- salvamento de histórico
- adição de persona para o assistente
- deploy da aplicação
- refinamentos adicionais de usabilidade e layout

## Autora

Brunna Leite Felix
# chatbot-com-ia
