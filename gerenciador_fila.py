import json

from gerenciador_email import enviar_email
from gerenciador_log import registrar_no_log_txt
from interface_usuario import selecionar_corpo, selecionar_anexo


NOME_ARQUIVO_FILA = "fila_de_envio.json"

def adicionar_email_a_fila():
    print("\n--- Adicionar E-mail à Fila de Envio ---")
    
    destinatario = input("Destinatário: ")
    titulo = input("Título do e-mail (Assunto): ")

    corpo = selecionar_corpo()
    if corpo is None: return

    caminho_anexo = selecionar_anexo()
    if caminho_anexo is None: return

    novo_email = {
        "destinatario": destinatario,
        "titulo": titulo,
        "corpo": corpo,
        "caminho_anexo": caminho_anexo
    }

    fila = _carregar_fila_json()
    fila.append(novo_email)
    _salvar_fila_json(fila)
    
    print("\n>>> E-mail adicionado à fila com sucesso! <<<")


def enviar_emails_da_fila():
    print("\n--- Enviar TODOS os E-mails da Fila ---")
    
    fila = _carregar_fila_json()
    if not fila:
        print("A fila de envio está vazia.")
        return

    print(f"Você tem {len(fila)} e-mail(s) na fila para enviar.")
    if input("Deseja enviar todos agora? (s/n): ").lower() != 's':
        print("Envio cancelado.")
        return

    print("\nIniciando o envio...")
    nao_enviados = []

    for i, email_data in enumerate(fila, 1):
        print(f"\nEnviando e-mail {i}/{len(fila)} para: {email_data['destinatario']}")
        try:
            enviar_email(
                email_data['destinatario'],
                email_data['titulo'],
                email_data['corpo'],
                email_data['caminho_anexo']
            )
            registrar_no_log_txt(email_data)
        except Exception as e:
            print(f"  Falha ao enviar para {email_data['destinatario']}. Erro: {e}")
            nao_enviados.append(email_data)

    _salvar_fila_json(nao_enviados)
    
    num_sucessos = len(fila) - len(nao_enviados)
    if num_sucessos > 0:
        print(f"\n{num_sucessos} e-mail(s) foram enviados e registrados no log.")

    if nao_enviados:
        print(f"{len(nao_enviados)} e-mail(s) não puderam ser enviados e permaneceram na fila.")
    else:
        print("Todos os e-mails foram enviados. A fila está limpa!")


def verificar_fila():
    print("\n--- Fila de Envio Atual ---")
    
    fila = _carregar_fila_json()
    if not fila:
        print("A fila de envio está vazia.")
        return

    for i, email_data in enumerate(fila, 1):
        print(f"\n--- E-mail {i} (Aguardando Envio) ---")
        print(f"  Destinatário: {email_data['destinatario']}")
        print(f"  Título: {email_data['titulo']}")
        print(f"  Anexo: email_data.get('caminho_anexo', 'N/A').split('/')[-1].split('\\')[-1]")
        print("-" * 20)


def _carregar_fila_json():
    try:
        with open(NOME_ARQUIVO_FILA, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar_fila_json(fila):
    with open(NOME_ARQUIVO_FILA, 'w', encoding='utf-8') as arquivo:
        json.dump(fila, arquivo, indent=4, ensure_ascii=False)
