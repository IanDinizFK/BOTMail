from datetime import datetime


NOME_ARQUIVO_LOG = "log_de_envios.txt"

def registrar_no_log_txt(email_data):
    hoje_str = datetime.now().strftime("%d/%m/%Y")
    header_dia = f"============={hoje_str}==============\n"
    
    hora_envio = datetime.now().strftime("%H:%M:%S")
    log_entry = (
        f"EMAIL ENVIADO {hora_envio}\n"
        f"  - Destinatário: {email_data['destinatario']}\n"
        f"  - Título: {email_data['titulo']}\n"
        f"  - Anexo: email_data.get('caminho_anexo', 'N/A').split('/')[-1].split('\\')[-1]\n\n"
    )
    
    try:
        with open(NOME_ARQUIVO_LOG, 'a+', encoding='utf-8') as arquivo:
            arquivo.seek(0)
            conteudo = arquivo.read()
            if header_dia not in conteudo:
                arquivo.write(header_dia)
            arquivo.write(log_entry)
    except IOError as e:
        print(f"Erro ao escrever no arquivo de log: {e}")

def verificar_historico():
    print("\n--- Histórico de Envios ---")
    try:
        with open(NOME_ARQUIVO_LOG, 'r', encoding='utf-8') as arquivo:
            log_conteudo = arquivo.read()
            if not log_conteudo.strip():
                print("Nenhum e-mail foi enviado ainda.")
            else:
                print(log_conteudo)
    except FileNotFoundError:
        print("O arquivo de log ainda não existe. Envie um e-mail para criá-lo.")
