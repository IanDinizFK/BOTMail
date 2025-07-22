# BOT de Envio de Currículos com API do Gmail

Este é um bot de linha de comando em Python projetado para automatizar e organizar o processo de envio de currículos e candidaturas por e-mail. Ele utiliza a API do Gmail para um envio seguro e robusto, e permite a criação de uma fila de e-mails personalizados para envio em massa.

## Funcionalidades

- **Fila de Envio:** Prepare múltiplos e-mails personalizados (destinatário, título, corpo, anexo) e envie todos de uma vez.
- **Templates de Corpo:** Crie e utilize templates de corpo de e-mail a partir de arquivos `.txt`.
- **Seleção de Anexos:** Selecione facilmente qual currículo (ou outro arquivo PDF) anexar a partir de uma pasta local.
- **Log de Envios:** Mantém um histórico legível de todos os e-mails enviados, agrupado por data.
- **Autenticação Segura:** Utiliza o protocolo OAuth 2.0 para se conectar à sua conta do Gmail, sem nunca expor sua senha principal.

---

## Guia de Instalação e Configuração

Siga estes passos para configurar e executar o bot em sua máquina local.

> **RECOMENDADO!**
>
> Caso prefira um guia visual, disponibilizo uma vídeo aula que é extremamente recomendável para acompanhar a configuração da Google Cloud.
>
> 🎬 **Link da Aula:** _[Em breve](https://www.youtube.com/)_

### 1. Pré-requisitos

- **Python 3.8 ou superior:** Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

### 2. Configuração do Projeto

1.  **Clone ou baixe este repositório:**
    ```bash
    git clone https://github.com/IanDinizFK/BOTMail.git
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Instale as dependências necessárias:**
    ```bash
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

### 3. Configuração da API do Google (Passo Essencial)

Para que o bot possa enviar e-mails em seu nome, você precisa autorizá-lo através da API do Gmail.

1.  **Acesse o Google Cloud Console:** Vá para o [Google Cloud Console](https://console.cloud.google.com/) e faça login com sua conta do Google.

2.  **Crie um Novo Projeto:** Se você ainda não tiver um, crie um novo projeto (ex: "Bot de E-mail").

3.  **Ative a API do Gmail:**
    - No menu de busca, procure por "Gmail API" e acesse a página da API.
    - Clique no botão **ATIVAR**.

4.  **Crie as Credenciais OAuth 2.0:**
    - No menu lateral esquerdo, navegue para **APIs e serviços > Tela de consentimento OAuth**.
        - Selecione **Externo** e clique em **CRIAR**.
        - Preencha as informações obrigatórias (Nome do app, E-mail de suporte do usuário) e salve. Não precisa preencher o resto.
        - Na tela de "Escopos", não precisa adicionar nada.
        - Na tela de "Usuários de teste", adicione seu próprio endereço de e-mail.
    - Agora, no menu lateral, vá para **APIs e serviços > Credenciais**.
        - Clique em **+ CRIAR CREDENCIAIS** e selecione **ID do cliente OAuth**.
        - No campo **"Tipo de aplicativo"**, selecione **"App para computador"**.
        - Dê um nome (ex: "Credencial Bot Desktop") e clique em **CRIAR**.

5.  **Baixe e Renomeie o Arquivo de Credenciais:**
    - Após a criação, uma janela aparecerá. Clique em **FAZER O DOWNLOAD DO JSON**.
    - Pegue o arquivo baixado, mova-o para a pasta raiz do seu projeto e **renomeie-o para `credentials.json`**.

### 4. Estrutura de Pastas e Arquivos

Antes de executar, prepare a estrutura de pastas do projeto:

1.  Coloque seus currículos (em formato `.pdf`) dentro da pasta anexos (um anexo por vez é permitido no envio) *OBS: CRIE A PASTA CASO NÃO EXISTA.
2.  Coloque seus modelos (bodys) de e-mail (em formato `.txt`) dentro da pasta corpos, já existe um arquivo txt dentro que você pode altera-lo.

### 5. Primeira Execução (Autorização)

Na primeira vez que você tentar enviar um e-mail, o bot precisará da sua permissão.

1.  Execute o bot no seu terminal:
    ```bash
    python bot.py
    ```
2.  Navegue pelo menu e tente enviar um e-mail.
3.  Uma **aba do seu navegador será aberta automaticamente**.
4.  Siga os passos na tela: escolha sua conta do Google (A MESMA QUE VOCÊ COLOCOU COMO USUÁRIO DE TESTE NA TELA 0AUTH) e clique em **Permitir** para conceder ao bot a permissão de enviar e-mails.
5.  Após a autorização, um arquivo `token.json` será criado na pasta do projeto. Ele armazena sua permissão, e você não precisará fazer isso novamente (a menos que apague o arquivo).

### 6. Como Usar

- **Opção 1:** Adiciona um e-mail completamente personalizado (destinatário, título, corpo e anexo) à fila de envio.
- **Opção 2:** Dispara o envio de todos os e-mails que estão na fila. Após o envio, a fila é limpa e os envios bem-sucedidos são registrados no `log_de_envios.txt`.
- **Opção 3:** Mostra um resumo dos e-mails que estão aguardando na fila.
- **Opção 4:** Exibe o conteúdo do `log_de_envios.txt`, mostrando todo o seu histórico de candidaturas.
