import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
NOME_ARQUIVO_CREDENCIAL = 'credentials.json'
NOME_ARQUIVO_TOKEN = 'token.json'

def autenticar():
    """
    Realiza a autenticação com a API do Gmail.
    Cria ou atualiza o arquivo token.json com as credenciais de acesso.
    """
    creds = None
    if os.path.exists(NOME_ARQUIVO_TOKEN):
        creds = Credentials.from_authorized_user_file(NOME_ARQUIVO_TOKEN, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(NOME_ARQUIVO_CREDENCIAL, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(NOME_ARQUIVO_TOKEN, 'w') as token:
            token.write(creds.to_json())
    
    return creds

def enviar_email(destinatario, assunto, corpo, caminho_anexo=None):
    creds = autenticar()
    
    try:
        service = build('gmail', 'v1', credentials=creds)
        
        message = MIMEMultipart()
        message['To'] = destinatario
        message['From'] = 'me' 
        message['Subject'] = assunto
        
        message.attach(MIMEText(corpo, 'plain'))
        
        if caminho_anexo and os.path.exists(caminho_anexo):
            nome_arquivo = os.path.basename(caminho_anexo)
            with open(caminho_anexo, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{nome_arquivo}"')
            message.attach(part)

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        create_message = {'raw': encoded_message}
        
        send_message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f"E-mail enviado com sucesso! ID da Mensagem: {send_message['id']}")

    except HttpError as error:
        print(f'Ocorreu um erro ao enviar o e-mail: {error}')
        raise error 

