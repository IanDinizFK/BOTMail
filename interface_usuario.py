import os

PASTA_ANEXOS = "anexos"
PASTA_CORPOS = "corpos"

def selecionar_corpo():
    print("\n--- Selecione o Corpo do E-mail ---")
    try:
        corpos = [f for f in os.listdir(PASTA_CORPOS) if f.endswith(".txt")]
    except FileNotFoundError:
        print(f"ERRO: A pasta '{PASTA_CORPOS}' não foi encontrada.")
        return None

    if not corpos:
        print("Nenhum template de corpo encontrado na pasta 'corpos'.")
    else:
        for i, nome_arquivo in enumerate(corpos, 1):
            print(f"{i}. Usar template '{nome_arquivo}'")

    print(f"{len(corpos) + 1}. Digitar um corpo de e-mail customizado")
    
    while True:
        try:
            escolha = int(input("Sua escolha: "))
            if 1 <= escolha <= len(corpos):
                caminho_completo = os.path.join(PASTA_CORPOS, corpos[escolha - 1])
                with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
                    return arquivo.read()
            elif escolha == len(corpos) + 1:
                print("\nDigite o corpo do seu e-mail (pressione Enter duas vezes para finalizar):")
                linhas = []
                while True:
                    linha = input()
                    if not linha:
                        break
                    linhas.append(linha)
                return "\n".join(linhas)
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número válido.")

def selecionar_anexo():
    print("\n--- Selecione o Anexo (Currículo) ---")
    try:
        anexos_pdf = [f for f in os.listdir(PASTA_ANEXOS) if f.lower().endswith(".pdf")]
    except FileNotFoundError:
        print(f"ERRO: A pasta '{PASTA_ANEXOS}' não foi encontrada.")
        return None

    if not anexos_pdf:
        print(f"ERRO: Nenhum arquivo PDF encontrado na pasta '{PASTA_ANEXOS}'. Adicione seu currículo lá.")
        return None

    for i, nome_arquivo in enumerate(anexos_pdf, 1):
        print(f"{i}. {nome_arquivo}")

    while True:
        try:
            escolha = int(input("Qual anexo você quer enviar? "))
            if 1 <= escolha <= len(anexos_pdf):
                return os.path.join(PASTA_ANEXOS, anexos_pdf[escolha - 1])
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número válido.")
