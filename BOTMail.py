import json
import os

from gerenciador_fila import adicionar_email_a_fila, enviar_emails_da_fila, verificar_fila
from gerenciador_log import verificar_historico

PASTA_ANEXOS = "anexos"
PASTA_CORPOS = "corpos"
NOME_ARQUIVO_FILA = "fila_de_envio.json"
NOME_ARQUIVO_LOG = "log_de_envios.txt"

def mostrar_menu():
    while True:
        with open(NOME_ARQUIVO_FILA, 'r') as f:
            try:
                num_na_fila = len(json.load(f))
            except:
                num_na_fila = 0

        print("\n=========== BOT DE ENVIO DE CURRÍCULO ===========")
        print(f"-- Fila Atual: {num_na_fila} e-mail(s) aguardando envio --")
        print("[1]✍  Adicionar e-mail à fila")
        print("[2]📩 Enviar TODOS os e-mails da fila")
        print("[3]📜 Verificar fila de envio")
        print("[4]📂 Verificar histórico de envios")
        print("[5]❌ Sair")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            adicionar_email_a_fila()
        elif escolha == '2':
            enviar_emails_da_fila()
        elif escolha == '3':
            verificar_fila()
        elif escolha == '4':
            verificar_historico()
        elif escolha == '5':
            print("Saindo do programa. Boa sorte com as vagas!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def main():
    print("Iniciando o Bot de E-mails...")
    
    for pasta in [PASTA_ANEXOS, PASTA_CORPOS]:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
    
    if not os.path.exists(NOME_ARQUIVO_FILA):
        with open(NOME_ARQUIVO_FILA, 'w') as f:
            json.dump([], f)
        
    if not os.path.exists(NOME_ARQUIVO_LOG):
        open(NOME_ARQUIVO_LOG, 'w').close()
        
    mostrar_menu()

if __name__ == "__main__":
    main()
